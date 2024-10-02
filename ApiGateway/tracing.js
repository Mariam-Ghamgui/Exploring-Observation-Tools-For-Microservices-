const opentelemetry = require('@opentelemetry/sdk-node');
const { getNodeAutoInstrumentations } = require('@opentelemetry/auto-instrumentations-node');
const { OTLPTraceExporter } = require('@opentelemetry/exporter-trace-otlp-http');
const { CompositeExporter } = require('@opentelemetry/exporter-trace-otlp-http');

const signozExporter = new OTLPTraceExporter({
  url: 'http://my-release-otel-collector.signoz.svc.cluster.local:4318/v1/traces',
});

const corootExporter = new OTLPTraceExporter({
  url: 'http://coroot-otel-collector.coroot.svc.cluster.local:4318/v1/traces',
});

const compositeExporter = new CompositeExporter([signozExporter, corootExporter]);

const sdk = new opentelemetry.NodeSDK({
  traceExporter: compositeExporter,
  instrumentations: [getNodeAutoInstrumentations()]
});

sdk.start();