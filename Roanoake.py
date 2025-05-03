import pandas as pd
import json

# Load the Excel data
file_path = '/home/ugrads/majors/jtvinh/cs2104/project/aadt_080_roanoke_2023.xlsx'
df = pd.read_excel(file_path, engine='openpyxl')

# Inspect structure (print columns and first rows)
print("Columns in the dataset:")
print(df.columns.tolist())
print("\nFirst 5 rows:")
print(df.head())

# Convert DataFrame to HTML table
table_html = df.to_html(classes='display', table_id='traffic-table', index=True)

# Prepare data for chart
# Assuming columns 'Segment' and 'AADT' exist; otherwise use first two columns
if 'Segment' in df.columns and 'AADT' in df.columns:
    labels = df['Segment'].astype(str).tolist()
    data_values = df['AADT'].tolist()
else:
    labels = df.iloc[:, 0].astype(str).tolist()
    data_values = df.iloc[:, 1].tolist()

labels_json = json.dumps(labels)
data_json = json.dumps(data_values)

# Build full HTML content
html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset='utf-8'>
  <title>AADT Report</title>
  <!-- Include DataTables CSS -->
  <link rel="stylesheet" type="text/css" href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css">
  <!-- Include Chart.js -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
  <style>
    table {{ border-collapse: collapse; width: 100%; margin: 1em auto; }}
    th, td {{ padding: 0.5em; border: 1px solid #290707; text-align: left; }}
    th {{ background: #a73c3c; }}
    .chart-container {{ width: 80%; margin: 2em auto; }}
  </style>
</head>
<body>
  <h1 style='text-align:center;'>AADT Report</h1>

  <!-- Table -->
  {table_html}

  <!-- Chart for AADT -->
  <div class="chart-container">
    <canvas id="aadtChart"></canvas>
  </div>

  <!-- Include jQuery and DataTables JS -->
  <script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
  <script src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>

  <script>
    $(document).ready(function() {{
      $('#traffic-table').DataTable();
    }});

    const ctx = document.getElementById('aadtChart').getContext('2d');
    new Chart(ctx, {{
      type: 'bar',
      data: {{
        labels: {labels_json},
        datasets: [{{
          label: 'AADT',
          data: {data_json},
          backgroundColor: 'rgba(54, 162, 235, 0.2)',
          borderColor: 'rgba(54, 162, 235, 1)',
          borderWidth: 1
        }}]
      }},
      options: {{
        responsive: true,
        scales: {{
          y: {{
            beginAtZero: true
          }}
        }}
      }}
    }});
  </script>
</body>
</html>"""

# Save HTML to file
html_file_path = '/home/ugrads/majors/jtvinh/cs2104/project/Roanoake_report.html'
with open(html_file_path, 'w') as f:
    f.write(html_content)

print(f"Generated HTML report at: {html_file_path}")
