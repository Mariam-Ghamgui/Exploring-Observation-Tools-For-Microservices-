from flask import Flask, jsonify
import random
from opentelemetry import trace
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource

QUOTES_FILE = "./quotes.txt"
quotes = []

# a quote
class Quote(object):
    def __init__(self, quote, by):
        self.quote = quote
        self.by = by

# Loads quotes from a file
def loadQuotes():
    with open(QUOTES_FILE) as file:
        lines = file.readlines()
        lines = [x.strip() for x in lines] 
        for line in lines:
            quote, by = line.split("-")
            quotes.append(Quote(quote, by))

app = Flask(__name__)

# Set up OpenTelemetry
resource = Resource(attributes={
    SERVICE_NAME: "quotes-service"
})

trace.set_tracer_provider(TracerProvider(resource=resource))

signoz_exporter = OTLPSpanExporter(endpoint="http://my-release-otel-collector.signoz.svc.cluster.local:4317")
coroot_exporter = OTLPSpanExporter(endpoint="http://coroot-otel-collector.coroot.svc.cluster.local:4317")

trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(signoz_exporter))
trace.get_tracer_provider().add_span_processor(BatchSpanProcessor(coroot_exporter))

# Instrument Flask
FlaskInstrumentor().instrument_app(app)

# Gets a random quote 
@app.route("/api/quote")
def quote():
    q = random.choice(quotes) # selects a random quote from file
    return jsonify({"quote": q.quote, "by": q.by}) # return a quote

# 404 Error for unknown routes
@app.errorhandler(404)
def page_not_found(e):
    return jsonify({"message": "Resource not found"}), 404

if __name__ == '__main__':
    loadQuotes()
    app.run(host='0.0.0.0', port=5000, debug=True)