import React from 'react';
import Plot from 'react-plotly.js';

function ChartComponent({ data, layout, config }) {
  return (
    <Plot
      data={data}
      layout={layout}
      config={config || {}} // Provide default config if not passed
    />
  );
}

export default ChartComponent;