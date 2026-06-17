const dashboardDataPath = "../results/dashboard_data.csv";
const executiveSummaryPath = "../results/executive_summary.md";
const eventInsightsPath = "../results/event_insights.json";
const llmContextPath = "../results/llm_context.json";
const historicalComparisonPath = "../results/historical_comparison.json";
const executiveBriefPath = "../results/executive_brief.json";
const newsDatabaseSummaryPath = "../results/news_database_summary.json";
const eventFamilySummaryPath = "../results/event_family_summary.json";
const scenarioSimilarityPath = "../results/scenario_similarity_results.json";
const historicalAnalogDemoPath = "../results/historical_analog_engine/demo_results.json";
const scenarioComparisonPath = "../results/scenario_comparison_engine/comparison_results.json";
const dataValidationPath = "../results/data_validation_report.json";

const formatPercent = (value) => {
  const number = Number(value);
  if (Number.isNaN(number)) return "N/A";
  return `${number.toFixed(2)}%`;
};

const formatScore = (value) => {
  const number = Number(value);
  if (Number.isNaN(number)) return "N/A";
  return number.toFixed(1);
};

const parseCsv = (text) => {
  const rows = text.trim().split(/\r?\n/);
  const headers = rows.shift().split(",");
  return rows.map((row) => {
    const values = row.split(",");
    return headers.reduce((record, header, index) => {
      record[header] = values[index] ?? "";
      return record;
    }, {});
  });
};

const getStrongestPositive = (events) =>
  events
    .filter((event) => event.status === "success" && Number(event.car_value) > 0)
    .sort((a, b) => Number(b.car_value) - Number(a.car_value))[0];

const getStrongestNegative = (events) =>
  events
    .filter((event) => event.status === "success" && Number(event.car_value) < 0)
    .sort((a, b) => Number(a.car_value) - Number(b.car_value))[0];

const renderKpiCards = (events) => {
  const totalEvents = events.length;
  const successfulEvents = events.filter((event) => event.status === "success").length;
  const failedEvents = events.filter((event) => event.status === "failed").length;
  const strongestPositive = getStrongestPositive(events);
  const strongestNegative = getStrongestNegative(events);

  const cards = [
    {
      label: "Total Events",
      value: totalEvents,
      note: "Events included in dashboard_data.csv",
    },
    {
      label: "Successful Events",
      value: successfulEvents,
      note: "Processed by Repo 2 engine",
    },
    {
      label: "Failed Events",
      value: failedEvents,
      note: "Recorded without stopping the batch",
    },
    {
      label: "Strongest Positive",
      value: strongestPositive?.event_name ?? "N/A",
      note: strongestPositive ? formatPercent(strongestPositive.car_percent) : "",
    },
    {
      label: "Strongest Negative",
      value: strongestNegative?.event_name ?? "N/A",
      note: strongestNegative ? formatPercent(strongestNegative.car_percent) : "",
    },
    {
      label: "Dashboard Status",
      value: "V1",
      note: "Deterministic intelligence layer",
    },
  ];

  document.getElementById("kpiCards").innerHTML = cards
    .map(
      (card) => `
        <div class="kpi-card">
          <p class="kpi-label">${card.label}</p>
          <p class="kpi-value">${card.value}</p>
          <p class="kpi-note">${card.note}</p>
        </div>
      `,
    )
    .join("");
};

const renderLatestEvent = (events) => {
  const sortedEvents = [...events].sort(
    (a, b) => new Date(b.event_date) - new Date(a.event_date),
  );
  const latestEvent = sortedEvents[0];
  if (!latestEvent) return;

  document.getElementById("latestEventTitle").textContent = latestEvent.event_name;
  const directionClass = `direction-${latestEvent.car_direction.toLowerCase()}`;
  const details = [
    ["Event Date", latestEvent.event_date],
    ["Mechanism", latestEvent.mechanism],
    ["Event Type", latestEvent.event_type],
    ["Asset / Benchmark", `${latestEvent.asset} / ${latestEvent.benchmark}`],
    ["CAR Percent", formatPercent(latestEvent.car_percent)],
    [
      "CAR Direction",
      `<span class="${directionClass}">${latestEvent.car_direction}</span>`,
    ],
    ["Status", latestEvent.status],
    ["Report", latestEvent.report_path],
  ];

  document.getElementById("latestEventDetails").innerHTML = details
    .map(
      ([label, value]) => `
        <div class="detail-item">
          <p class="detail-label">${label}</p>
          <p class="detail-value">${value}</p>
        </div>
      `,
    )
    .join("");
};

const renderMarkdown = (markdown) => {
  const lines = markdown.split(/\r?\n/);
  let html = "";
  let inList = false;
  let inTable = false;
  let tableRows = [];

  const closeList = () => {
    if (inList) {
      html += "</ul>";
      inList = false;
    }
  };

  const closeTable = () => {
    if (!inTable) return;
    const [header, separator, ...body] = tableRows;
    const headerCells = header
      .split("|")
      .filter(Boolean)
      .map((cell) => `<th>${cell.trim()}</th>`)
      .join("");
    const bodyRows = body
      .filter((row) => row !== separator)
      .map((row) => {
        const cells = row
          .split("|")
          .filter(Boolean)
          .map((cell) => `<td>${cell.trim()}</td>`)
          .join("");
        return `<tr>${cells}</tr>`;
      })
      .join("");
    html += `<table><thead><tr>${headerCells}</tr></thead><tbody>${bodyRows}</tbody></table>`;
    tableRows = [];
    inTable = false;
  };

  lines.forEach((line) => {
    if (line.startsWith("|")) {
      closeList();
      inTable = true;
      tableRows.push(line);
      return;
    }

    closeTable();

    if (line.startsWith("# ")) {
      closeList();
      html += `<h1>${line.replace("# ", "")}</h1>`;
    } else if (line.startsWith("## ")) {
      closeList();
      html += `<h2>${line.replace("## ", "")}</h2>`;
    } else if (line.startsWith("- ")) {
      if (!inList) {
        html += "<ul>";
        inList = true;
      }
      html += `<li>${line.replace("- ", "")}</li>`;
    } else if (line.trim()) {
      closeList();
      html += `<p>${line}</p>`;
    }
  });

  closeList();
  closeTable();
  return html;
};

const renderInsights = (insightData) => {
  const insightCards = document.getElementById("insightCards");
  const insights = insightData.insights ?? [];

  if (!insights.length) {
    insightCards.innerHTML =
      '<div class="insight-card"><p class="insight-title">No rule-based insights generated.</p></div>';
    return;
  }

  insightCards.innerHTML = insights
    .map(
      (insight) => `
        <article class="insight-card">
          <p class="insight-category">${insight.category}</p>
          <h3>${insight.title}</h3>
          <p class="insight-event">${insight.event_name} (${insight.event_id})</p>
          <p>${insight.explanation}</p>
          <dl class="evidence-list">
            <div>
              <dt>Rule</dt>
              <dd>${insight.evidence.rule}</dd>
            </div>
            <div>
              <dt>CAR</dt>
              <dd>${insight.evidence.car_percent}</dd>
            </div>
            ${
              insight.evidence.mechanism_mean_percent
                ? `<div><dt>Mechanism Avg.</dt><dd>${insight.evidence.mechanism_mean_percent}</dd></div>`
                : ""
            }
          </dl>
          <p class="insight-note">${insight.use_note}</p>
        </article>
      `,
    )
    .join("");
};

const renderContextSummary = (contextData) => {
  const runSummary = contextData.run_summary ?? {};
  const sourceFiles = contextData.source_files ?? [];
  const constraints = contextData.use_constraints ?? [];

  const items = [
    ["Events", runSummary.event_count ?? "N/A"],
    ["Successful", runSummary.successful_event_count ?? "N/A"],
    ["Failed", runSummary.failed_event_count ?? "N/A"],
    ["Sources", sourceFiles.join(", ")],
    ["Constraints", constraints.join("; ")],
    ["Purpose", contextData.purpose ?? "N/A"],
  ];

  document.getElementById("contextSummary").innerHTML = items
    .map(
      ([label, value]) => `
        <div class="detail-item">
          <p class="detail-label">${label}</p>
          <p class="detail-value">${value}</p>
        </div>
      `,
    )
    .join("");
};

const renderNewsDatabaseSummary = (summaryData) => {
  const eventFamilyCounts = summaryData.count_by_event_family ?? {};
  const actorCounts = summaryData.count_by_actor ?? {};
  const topEventFamilies = Object.entries(eventFamilyCounts)
    .sort(([, a], [, b]) => Number(b) - Number(a))
    .slice(0, 3)
    .map(([family, count]) => `${family} (${count})`)
    .join(", ");
  const actorsCovered = Object.keys(actorCounts).join("; ");

  const items = [
    ["Total News Items", summaryData.news_item_count ?? "N/A"],
    ["Top Event Families", topEventFamilies || "N/A"],
    ["Actors Covered", actorsCovered || "N/A"],
    ["Average Relevance", summaryData.average_relevance_score ?? "N/A"],
  ];

  document.getElementById("newsDatabaseSummary").innerHTML = items
    .map(
      ([label, value]) => `
        <div class="detail-item">
          <p class="detail-label">${label}</p>
          <p class="detail-value">${value}</p>
        </div>
      `,
    )
    .join("");
};

const renderProjectMetadata = (validationData) => {
  const summary = validationData.summary ?? {};
  const status = validationData.status ?? "N/A";
  const items = [
    ["Events", summary.event_count ?? "N/A"],
    ["News Items", summary.news_item_count ?? "N/A"],
    ["Event Families", summary.event_family_count ?? "N/A"],
    ["Validation Status", status],
  ];

  document.getElementById("projectMetadata").innerHTML = items
    .map(
      ([label, value]) => `
        <div class="detail-item">
          <p class="detail-label">${label}</p>
          <p class="detail-value ${
            label === "Validation Status" ? `status-${String(value).toLowerCase()}` : ""
          }">${value}</p>
        </div>
      `,
    )
    .join("");
};

const renderEventFamilyAnalytics = (summaryData) => {
  const container = document.getElementById("eventFamilyAnalytics");
  const summaries = summaryData.summaries ?? [];

  if (!summaries.length) {
    container.innerHTML =
      '<div class="comparison-card"><p>No event-family analytics available.</p></div>';
    return;
  }

  container.innerHTML = summaries
    .map(
      (family) => `
        <article class="comparison-card">
          <p class="insight-category">${family.event_family}</p>
          <h3>${family.event_count} event(s), ${family.linked_news_count} linked news item(s)</h3>
          <dl class="evidence-list">
            <div>
              <dt>Average CAR</dt>
              <dd>${family.average_car === "" ? "N/A" : `${family.average_car}%`}</dd>
            </div>
            <div>
              <dt>Positive / Negative</dt>
              <dd>${family.positive_car_count} / ${family.negative_car_count}</dd>
            </div>
            <div>
              <dt>CAR Metric</dt>
              <dd>${family.car_metric || "N/A"}</dd>
            </div>
          </dl>
          <p class="insight-note">${family.interpretation_note}</p>
        </article>
      `,
    )
    .join("");
};

const renderTheoryLayer = (validationData) => {
  const container = document.getElementById("theoryLayer");
  const variables = validationData.theory_coverage?.variables ?? {};
  const labels = {
    interpretation_type: "Interpretation",
    state_support_signal: "State Support",
    strategic_importance_level: "Strategic Importance",
  };

  const cards = Object.entries(labels).map(([field, label]) => {
    const distribution = variables[field]?.distribution ?? {};
    const values = Object.entries(distribution)
      .map(([category, count]) => `${category}: ${count}`)
      .join("; ");
    return `
      <article class="comparison-card">
        <p class="insight-category">${label}</p>
        <h3>${values || "N/A"}</h3>
        <p class="insight-note">
          Coded: ${variables[field]?.coded_count ?? "N/A"};
          Uncoded: ${variables[field]?.uncoded_count ?? "N/A"}
        </p>
      </article>
    `;
  });

  container.innerHTML = cards.join("");
};

const renderScenarioSimilarity = (similarityData) => {
  const container = document.getElementById("scenarioSimilarity");
  const scenarios = similarityData.scenarios ?? [];

  if (!scenarios.length) {
    container.innerHTML =
      '<div class="comparison-card"><p>No scenario similarity results available.</p></div>';
    return;
  }

  container.innerHTML = scenarios
    .map((scenario) => {
      const matches = scenario.top_matches ?? [];
      return `
        <article class="scenario-card">
          <p class="insight-category">${scenario.scenario_id}</p>
          <h3>${scenario.scenario_text}</h3>
          <p class="insight-note">${scenario.caution_label}</p>
          <div class="scenario-match-list">
            ${matches
              .map((match) => {
                const carContext = match.historical_market_reaction?.label ?? "N/A";
                return `
                  <div class="scenario-match">
                    <p class="detail-label">${match.event_family}</p>
                    <h4>${match.event_title}</h4>
                    <dl class="evidence-list">
                      <div>
                        <dt>Similarity Score</dt>
                        <dd>${match.similarity_score}</dd>
                      </div>
                      <div>
                        <dt>Linked News</dt>
                        <dd>${match.linked_news_count}</dd>
                      </div>
                      <div>
                        <dt>Historical CAR</dt>
                        <dd>${carContext}</dd>
                      </div>
                    </dl>
                  </div>
                `;
              })
              .join("")}
          </div>
          <p class="insight-note">${scenario.interpretation_note}</p>
        </article>
      `;
    })
    .join("");
};

const renderScenarioIntelligenceFallback = (message) => {
  const container = document.getElementById("scenarioIntelligenceDemo");
  container.innerHTML = `
    <article class="scenario-demo-card">
      <p class="insight-category">Historical analog demo unavailable</p>
      <h3>Regenerate deterministic demo outputs</h3>
      <p>
        The dashboard could not load <code>results/historical_analog_engine/demo_results.json</code>.
        Run <code>python3 scripts/historical_analog_engine.py</code> from the repository root,
        then refresh this page.
      </p>
      <p class="insight-note">${message}</p>
      <p class="insight-note">
        Historical analog retrieval only. No forecasts, investment advice, or trading recommendations.
      </p>
    </article>
  `;
};

const renderScenarioIntelligenceDemo = (demoData) => {
  const container = document.getElementById("scenarioIntelligenceDemo");
  const questions = demoData.questions ?? [];

  if (!questions.length) {
    renderScenarioIntelligenceFallback("Demo JSON loaded, but no demo questions were found.");
    return;
  }

  container.innerHTML = questions
    .map((question) => {
      const scenario = question.mapped_scenario ?? {};
      const analogs = question.historical_analogs ?? [];
      const topAnalog = analogs[0] ?? {};
      const components = topAnalog.score_components ?? {};
      const evidenceItems = topAnalog.evidence_items ?? [];
      const pathways = topAnalog.observed_historical_pathways ?? [];
      const analystNotes = question.analyst_notes ?? [];

      const briefExplanation =
        Object.entries(components)
          .slice(0, 4)
          .map(([, component]) => component.explanation)
          .filter(Boolean)
          .join(" ")
        || "Similarity explanation unavailable for this demo question.";

      return `
        <article class="scenario-demo-card">
          <div class="scenario-demo-header">
            <div>
              <p class="insight-category">${scenario.scenario_id ?? "Scenario"}</p>
              <h3>${question.question}</h3>
            </div>
            <span class="classification-badge">${scenario.event_family ?? "Unclassified"}</span>
          </div>

          <dl class="scenario-classification">
            <div>
              <dt>Scenario Classification</dt>
              <dd>${scenario.event_family ?? "N/A"}</dd>
            </div>
            <div>
              <dt>Actors</dt>
              <dd>${(scenario.actors ?? []).join("; ") || "N/A"}</dd>
            </div>
            <div>
              <dt>Targets</dt>
              <dd>${(scenario.targets ?? []).join("; ") || "N/A"}</dd>
            </div>
          </dl>

          <h4>Top Historical Analogs</h4>
          <div class="analog-table-wrap">
            <table class="analog-table">
              <thead>
                <tr>
                  <th>Rank</th>
                  <th>Event</th>
                  <th>Family</th>
                  <th>Score</th>
                  <th>Confidence</th>
                </tr>
              </thead>
              <tbody>
                ${analogs
                  .slice(0, 3)
                  .map(
                    (analog, index) => `
                      <tr>
                        <td>${index + 1}</td>
                        <td>${analog.event_id} - ${analog.event_name}</td>
                        <td>${analog.event_family}</td>
                        <td>${formatScore(analog.similarity_score)}</td>
                        <td>${analog.confidence}</td>
                      </tr>
                    `,
                  )
                  .join("")}
              </tbody>
            </table>
          </div>

          <div class="scenario-demo-grid">
            <section>
              <h4>Brief Similarity Explanation</h4>
              <p>${briefExplanation}</p>
              <p class="insight-note">
                Top analog: ${topAnalog.event_id ?? "N/A"} - ${topAnalog.event_name ?? "N/A"}.
                Similarity score ${formatScore(topAnalog.similarity_score)}.
              </p>
            </section>

            <section>
              <h4>Evidence Base</h4>
              <ul>
                <li>Event source: ${topAnalog.source || "N/A"}</li>
                ${
                  evidenceItems.length
                    ? evidenceItems
                        .slice(0, 2)
                        .map(
                          (item) =>
                            `<li>${item.news_id}: ${item.source} - ${item.title}</li>`,
                        )
                        .join("")
                    : "<li>Linked news evidence: none in current demo output.</li>"
                }
              </ul>
            </section>

            <section>
              <h4>Observed Historical Pathways</h4>
              <ul>
                ${
                  pathways.length
                    ? pathways.slice(0, 3).map((pathway) => `<li>${pathway}</li>`).join("")
                    : "<li>No observed pathway summary available.</li>"
                }
              </ul>
            </section>

            <section>
              <h4>Analyst Notes</h4>
              <ul>
                ${
                  analystNotes.length
                    ? analystNotes.slice(0, 4).map((note) => `<li>${note}</li>`).join("")
                    : "<li>Historical analog retrieval only. No forecasts or investment recommendations.</li>"
                }
              </ul>
            </section>
          </div>
        </article>
      `;
    })
    .join("");
};

const renderScenarioComparisonFallback = (message) => {
  const container = document.getElementById("scenarioComparisonView");
  container.innerHTML = `
    <article class="scenario-comparison-card">
      <p class="insight-category">Scenario comparison unavailable</p>
      <h3>Regenerate deterministic comparison outputs</h3>
      <p>
        The dashboard could not load <code>results/scenario_comparison_engine/comparison_results.json</code>.
        Run <code>python3 scripts/scenario_comparison_engine.py</code> after regenerating historical analog outputs,
        then refresh this page.
      </p>
      <p class="insight-note">${message}</p>
      <p class="insight-note">
        Scenario comparison explains historical similarity and difference only.
        It does not forecast returns or provide investment recommendations.
      </p>
    </article>
  `;
};

const renderScenarioComparisonView = (comparisonData) => {
  const container = document.getElementById("scenarioComparisonView");
  const comparisons = comparisonData.comparisons ?? [];

  if (!comparisons.length) {
    renderScenarioComparisonFallback("Comparison JSON loaded, but no comparisons were found.");
    return;
  }

  container.innerHTML = comparisons
    .map((comparison) => {
      const cva = comparison.closest_vs_alternative ?? {};
      const closest = cva.closest_historical_analog ?? {};
      const alternative = cva.alternative_analog ?? {};
      const matrix = closest.comparison_matrix ?? [];
      const matching = closest.major_matching_features ?? [];
      const differences = closest.major_differences ?? [];

      return `
        <article class="scenario-comparison-card">
          <div class="scenario-demo-header">
            <div>
              <p class="insight-category">${comparison.mapped_scenario?.scenario_id ?? "Scenario"}</p>
              <h3>${comparison.question}</h3>
            </div>
            <span class="classification-badge">${comparison.mapped_scenario?.event_family ?? "N/A"}</span>
          </div>

          <div class="closest-grid">
            <div>
              <p class="detail-label">Closest Historical Analog</p>
              <p class="detail-value">${closest.event_id ?? "N/A"} - ${closest.event_name ?? "N/A"}</p>
              <p class="insight-note">Score ${formatScore(closest.similarity_score)}</p>
            </div>
            <div>
              <p class="detail-label">Alternative Analog</p>
              <p class="detail-value">${alternative.event_id ?? "N/A"} - ${alternative.event_name ?? "N/A"}</p>
              <p class="insight-note">Score ${formatScore(alternative.similarity_score)}</p>
            </div>
          </div>
          <p class="comparison-summary">${cva.comparison_summary ?? "No closest-vs-alternative summary available."}</p>

          <h4>Similarity Matrix</h4>
          <div class="analog-table-wrap">
            <table class="analog-table comparison-matrix-table">
              <thead>
                <tr>
                  <th>Dimension</th>
                  <th>Scenario</th>
                  <th>Historical Analog</th>
                  <th>Status</th>
                  <th>Explanation</th>
                </tr>
              </thead>
              <tbody>
                ${matrix
                  .map(
                    (row) => `
                      <tr>
                        <td>${row.dimension}</td>
                        <td>${row.query_value}</td>
                        <td>${row.historical_value}</td>
                        <td><span class="matrix-status matrix-${row.status}">${row.status}</span></td>
                        <td>${row.explanation}</td>
                      </tr>
                    `,
                  )
                  .join("")}
              </tbody>
            </table>
          </div>

          <div class="scenario-demo-grid">
            <section>
              <h4>Match Explanation</h4>
              <ul>
                ${
                  matching.length
                    ? matching.slice(0, 4).map((item) => `<li>${item}</li>`).join("")
                    : "<li>No major matching features available.</li>"
                }
              </ul>
            </section>
            <section>
              <h4>Key Differences</h4>
              <ul>
                ${
                  differences.length
                    ? differences.slice(0, 4).map((item) => `<li>${item}</li>`).join("")
                    : "<li>No major differences identified by deterministic rules.</li>"
                }
              </ul>
            </section>
          </div>
        </article>
      `;
    })
    .join("");
};

const renderHistoricalComparison = (comparisonData) => {
  const comparisons = comparisonData.comparisons ?? [];
  const container = document.getElementById("historicalComparison");

  if (!comparisons.length) {
    container.innerHTML =
      '<div class="insight-card"><p>No historical comparisons available.</p></div>';
    return;
  }

  container.innerHTML = comparisons
    .map(
      (comparison) => `
        <article class="comparison-card">
          <p class="insight-category">${comparison.relative_strength}</p>
          <h3>${comparison.event_name}</h3>
          <dl class="evidence-list">
            <div>
              <dt>Event CAR</dt>
              <dd>${comparison.event_car_percent}</dd>
            </div>
            <div>
              <dt>Mechanism Avg.</dt>
              <dd>${comparison.mechanism_average_percent}</dd>
            </div>
            <div>
              <dt>Magnitude Ratio</dt>
              <dd>${
                comparison.magnitude_ratio === null
                  ? "N/A"
                  : Number(comparison.magnitude_ratio).toFixed(2)
              }</dd>
            </div>
          </dl>
          <p>${comparison.interpretation}</p>
        </article>
      `,
    )
    .join("");
};

const renderExecutiveBrief = (briefData) => {
  const mechanismSummaries = briefData.mechanism_summaries ?? [];
  const highlights = briefData.highlights ?? [];
  const comparisonSummary = briefData.comparison_summary ?? {};

  document.getElementById("executiveBrief").innerHTML = `
    <p>${briefData.overview}</p>
    <h3>Highlights</h3>
    <ul>
      ${highlights.map((highlight) => `<li>${highlight}</li>`).join("")}
    </ul>
    <h3>Mechanism Summaries</h3>
    <ul>
      ${mechanismSummaries
        .map((summary) => `<li>${summary.summary}</li>`)
        .join("")}
    </ul>
    <h3>Comparison Summary</h3>
    <p>
      ${comparisonSummary.comparison_count ?? 0} comparison(s);
      ${comparisonSummary.stronger_than_average_count ?? 0} stronger than average;
      ${comparisonSummary.weaker_than_average_count ?? 0} weaker than average.
    </p>
    <p class="insight-note">${briefData.analyst_note}</p>
    <p class="insight-note">${briefData.restriction_note}</p>
  `;
};

const loadDashboard = async () => {
  try {
    const [
      csvResponse,
      summaryResponse,
      insightsResponse,
      contextResponse,
      comparisonResponse,
      briefResponse,
      newsSummaryResponse,
      eventFamilyResponse,
      scenarioSimilarityResponse,
      dataValidationResponse,
    ] = await Promise.all([
      fetch(dashboardDataPath),
      fetch(executiveSummaryPath),
      fetch(eventInsightsPath),
      fetch(llmContextPath),
      fetch(historicalComparisonPath),
      fetch(executiveBriefPath),
      fetch(newsDatabaseSummaryPath),
      fetch(eventFamilySummaryPath),
      fetch(scenarioSimilarityPath),
      fetch(dataValidationPath),
    ]);

    if (
      !csvResponse.ok ||
      !summaryResponse.ok ||
      !insightsResponse.ok ||
      !contextResponse.ok ||
      !comparisonResponse.ok ||
      !briefResponse.ok ||
      !newsSummaryResponse.ok ||
      !eventFamilyResponse.ok ||
      !scenarioSimilarityResponse.ok ||
      !dataValidationResponse.ok
    ) {
      throw new Error("Unable to load Repo 2 dashboard outputs.");
    }

    const events = parseCsv(await csvResponse.text());
    const executiveSummary = await summaryResponse.text();
    const insightData = await insightsResponse.json();
    const contextData = await contextResponse.json();
    const comparisonData = await comparisonResponse.json();
    const briefData = await briefResponse.json();
    const newsSummaryData = await newsSummaryResponse.json();
    const eventFamilyData = await eventFamilyResponse.json();
    const scenarioSimilarityData = await scenarioSimilarityResponse.json();
    const dataValidationData = await dataValidationResponse.json();

    renderKpiCards(events);
    renderLatestEvent(events);
    document.getElementById("executiveSummary").innerHTML =
      renderMarkdown(executiveSummary);
    renderInsights(insightData);
    renderContextSummary(contextData);
    renderProjectMetadata(dataValidationData);
    renderNewsDatabaseSummary(newsSummaryData);
    renderEventFamilyAnalytics(eventFamilyData);
    renderTheoryLayer(dataValidationData);
    renderScenarioSimilarity(scenarioSimilarityData);
    renderHistoricalComparison(comparisonData);
    renderExecutiveBrief(briefData);
  } catch (error) {
    document.getElementById("kpiCards").innerHTML =
      `<div class="kpi-card"><p class="kpi-value">Data unavailable</p><p class="kpi-note">${error.message}</p></div>`;
    document.getElementById("executiveSummary").textContent = error.message;
    document.getElementById("insightCards").textContent = error.message;
    document.getElementById("contextSummary").textContent = error.message;
    document.getElementById("projectMetadata").textContent = error.message;
    document.getElementById("newsDatabaseSummary").textContent = error.message;
    document.getElementById("eventFamilyAnalytics").textContent = error.message;
    document.getElementById("theoryLayer").textContent = error.message;
    document.getElementById("scenarioSimilarity").textContent = error.message;
    document.getElementById("historicalComparison").textContent = error.message;
    document.getElementById("executiveBrief").textContent = error.message;
  }
};

const loadScenarioIntelligenceDemo = async () => {
  try {
    const response = await fetch(historicalAnalogDemoPath);
    if (!response.ok) {
      throw new Error("Historical analog demo JSON could not be loaded.");
    }
    const demoData = await response.json();
    renderScenarioIntelligenceDemo(demoData);
  } catch (error) {
    renderScenarioIntelligenceFallback(error.message);
  }
};

const loadScenarioComparisonView = async () => {
  try {
    const response = await fetch(scenarioComparisonPath);
    if (!response.ok) {
      throw new Error("Scenario comparison JSON could not be loaded.");
    }
    const comparisonData = await response.json();
    renderScenarioComparisonView(comparisonData);
  } catch (error) {
    renderScenarioComparisonFallback(error.message);
  }
};

loadDashboard();
loadScenarioIntelligenceDemo();
loadScenarioComparisonView();
