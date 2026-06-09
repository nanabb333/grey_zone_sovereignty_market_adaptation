const dashboardDataPath = "../results/dashboard_data.csv";
const executiveSummaryPath = "../results/executive_summary.md";

const formatPercent = (value) => {
  const number = Number(value);
  if (Number.isNaN(number)) return "N/A";
  return `${number.toFixed(2)}%`;
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
      value: "MVP",
      note: "AI panel placeholder only",
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

const loadDashboard = async () => {
  try {
    const [csvResponse, summaryResponse] = await Promise.all([
      fetch(dashboardDataPath),
      fetch(executiveSummaryPath),
    ]);

    if (!csvResponse.ok || !summaryResponse.ok) {
      throw new Error("Unable to load Repo 2 dashboard outputs.");
    }

    const events = parseCsv(await csvResponse.text());
    const executiveSummary = await summaryResponse.text();

    renderKpiCards(events);
    renderLatestEvent(events);
    document.getElementById("executiveSummary").innerHTML =
      renderMarkdown(executiveSummary);
  } catch (error) {
    document.getElementById("kpiCards").innerHTML =
      `<div class="kpi-card"><p class="kpi-value">Data unavailable</p><p class="kpi-note">${error.message}</p></div>`;
    document.getElementById("executiveSummary").textContent = error.message;
  }
};

loadDashboard();
