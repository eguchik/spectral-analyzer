const inputFile = document.getElementById('inputFile');
const reader = new FileReader();
let spectra = [];
let sampleName = [];
let nSample = [];
let xdata = [];
let lines = [];
let layout = {};
let trace = {};
let colorGradation = [];



inputFile.addEventListener('change', (event) => {
  file = event.target.files[0];
  reader.readAsText(file);
})

reader.addEventListener('load', () => {
  row = reader.result.split('\n');
  row.pop();
  sampleName = row.shift().split(',');
  sampleName.shift();
  nSample = sampleName.length;

  let hueList = [...sampleName.keys()];
  hueList = hueList.map(x => Number(x));
  hueList = hueList.map(x => x * 280 /hueList[hueList.length-1]);

  for (const hue of hueList) {
      colorGradation.push(`hsl(${hue},100%,50%)`);
  }




  for (let i = 0; i < nSample+1; i++) {
    spectra[i] = [];
  }

  row.forEach((value) => {
    for (let i = 0; i < nSample+1; i++) {
      spectra[i].push(value.split(',')[i]);
    }
  })

  spectra.forEach((value) => {
    value.shift();
  })

  xdata = spectra.shift();

  for (let i = 0; i < nSample; i++) {
    trace = {
      x: xdata,
      y: spectra[i],
      type: 'scatter',
      mode: 'lines',
      name: sampleName[i],
      line: {
        width: 2,
        dash: 'solid'
      }
    }
    lines.push(trace)
  }

  layout = {
    colorway : colorGradation.reverse(),
    width: 800,
    height: 600,
    xaxis: {
      title: {text: 'Wavelength (nm)', font: {family: 'Arial', size: 20}},
      showgrid: false,
      showline: true,
      mirror: 'ticks',
      autotick: false,
      ticks: 'inside',
      tick0: 0,
      dtick: 100,
      ticklen: 4,
      tickwidth: 2,
      tickcolor: '#000000',
      linecolor: '#000000',
      linewidth: 2,
      tickfont: {family: 'Arial', size: 20},
    },
    yaxis: {
      title: {text: 'Absorbance', font: {family: 'Arial', size: 20}},
      showgrid: false,
      zeroline: true,
      showline: true,
      mirror: 'ticks',
      autotick: false,
      ticks: 'inside',
      tick0: 0,
      dtick: 0.1,
      ticklen: 4,
      tickwidth: 2,
      tickcolor: '#000000',
      zerolinecolor: '#000000',
      zerolinewidth: 2,
      linecolor: '#000000',
      linewidth: 2,
      tickfont: {family: 'Arial', size: 20},
    },
    legend: {
      borderwidth: 0,
      title: {text: '', font: {family: 'Arial', size: 20}},
    }
  };
  Plotly.newPlot('myDiv', lines, layout);


  let selectPlot = document.getElementById('selectPlot');
  for (value of sampleName) {
    let option = document.createElement('option');
    option.setAttribute('value', value);
    option.innerHTML = value;
    selectPlot.appendChild(option);
  };




})


const graphWidth = document.getElementById('graphWidth')
graphWidth.addEventListener('change', (event) => {
  layout.width = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const graphHeight = document.getElementById('graphHeight');
graphHeight.addEventListener('change', (event) => {
  layout.height = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisTitleText = document.getElementById('xAxisTitleText');
xAxisTitleText.addEventListener('change', (event) => {
  layout.xaxis.title.text = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisTitleFontSize = document.getElementById('xAxisTitleFontSize');
xAxisTitleFontSize.addEventListener('change', (event) => {
  layout.xaxis.title.font.size = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisTickfontSize = document.getElementById('xAxisTickfontSize');
xAxisTickfontSize.addEventListener('change', (event) => {
  layout.xaxis.tickfont.size = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisTicks = document.getElementById('xAxisTicks');
xAxisTicks.addEventListener('change', (event) => {
  layout.xaxis.ticks = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisDtick = document.getElementById('xAxisDtick');
xAxisDtick.addEventListener('change', (event) => {
  layout.xaxis.dtick = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisTicklen = document.getElementById('xAxisTicklen');
xAxisTicklen.addEventListener('change', (event) => {
  layout.xaxis.ticklen = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisTickwidth = document.getElementById('xAxisTickwidth');
xAxisTickwidth.addEventListener('change', (event) => {
  layout.xaxis.tickwidth = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const xAxisLinewidth = document.getElementById('xAxisLinewidth');
xAxisLinewidth.addEventListener('change', (event) => {
  layout.xaxis.linewidth = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})



const yAxisTitleText = document.getElementById('yAxisTitleText');
yAxisTitleText.addEventListener('change', (event) => {
  layout.yaxis.title.text = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisTitleFontSize = document.getElementById('yAxisTitleFontSize');
yAxisTitleFontSize.addEventListener('change', (event) => {
  layout.yaxis.title.font.size = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisTickfontSize = document.getElementById('yAxisTickfontSize');
yAxisTickfontSize.addEventListener('change', (event) => {
  layout.yaxis.tickfont.size = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisTicks = document.getElementById('yAxisTicks');
yAxisTicks.addEventListener('change', () => {
  layout.yaxis.ticks = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisDtick = document.getElementById('yAxisDtick');
yAxisDtick.addEventListener('change', (event) => {
  layout.yaxis.dtick = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisTicklen = document.getElementById('yAxisTicklen');
yAxisTicklen.addEventListener('change', (event) => {
  layout.yaxis.ticklen = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisTickwidth = document.getElementById('yAxisTickwidth');
yAxisTickwidth.addEventListener('change', (event) => {
  layout.yaxis.tickwidth = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisLinewidth = document.getElementById('yAxisLinewidth');
yAxisLinewidth.addEventListener('change', (event) => {
  layout.yaxis.linewidth = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisZeroline = document.getElementById('yAxisZeroline');
yAxisZeroline.addEventListener('change', (event) => {
  layout.yaxis.zeroline = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const yAxisZerolinewidth = document.getElementById('yAxisZerolinewidth');
yAxisZerolinewidth.addEventListener('change', (event) => {
  layout.yaxis.zerolinewidth = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})



const legendBorderwidth = document.getElementById('legendBorderwidth');
legendBorderwidth.addEventListener('change', (event) => {
  layout.legend.borderwidth = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const legendTitleText = document.getElementById('legendTitleText');
legendTitleText.addEventListener('change', (event) => {
  layout.legend.title.text = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const legendTitleSize = document.getElementById('legendTitleSize');
legendTitleSize.addEventListener('change', (event) => {
  layout.legend.title.size = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const legendX = document.getElementById('legendX');
legendX.addEventListener('change', (event) => {
  layout.legend.x = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})

const legendY = document.getElementById('legendY');
legendY.addEventListener('change', (event) => {
  layout.legend.y = event.target.value;
  Plotly.newPlot('myDiv', lines, layout);
})




// change line style
const traceLineColor = document.getElementById('traceLineColor');
traceLineColor.addEventListener('change', (event) => {
  const selectPlot = document.getElementById('selectPlot');
  value = selectPlot.value;
  for (let i = 0; i < nSample; i++) {
    if (lines[i].name == value) {
      lines[i].line.color = event.target.value;
      Plotly.newPlot('myDiv', lines, layout);
    }
  }
})

const traceLineWidth = document.getElementById('traceLineWidth');
traceLineWidth.addEventListener('change', (event) => {
  const selectPlot = document.getElementById('selectPlot');
  value = selectPlot.value;
  for (let i = 0; i < nSample; i++) {
    if (lines[i].name == value) {
      lines[i].line.width = event.target.value;
      Plotly.newPlot('myDiv', lines, layout);
    }
  }
})


const traceLineDash = document.getElementById('traceLineDash');
traceLineDash.addEventListener('change', (event) => {
  const selectPlot = document.getElementById('selectPlot');
  value = selectPlot.value;
  for (let i = 0; i < nSample; i++) {
    if (lines[i].name == value) {
      lines[i].line.dash = event.target.value;
      Plotly.newPlot('myDiv', lines, layout);
    }
  }
})


