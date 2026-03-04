# OTel API
from opentelemetry import trace as trace_api

# OTel SDK
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

# OTel Exporter
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import OTLPSpanExporter

def create_tracing_pipeline():
    otlp_exporter = OTLPSpanExporter(
        endpoint="http://localhost:4317",
        insecure=True
    )
    span_processor = BatchSpanProcessor(otlp_exporter)
    return span_processor

def create_tracer(name: str, version: str) -> trace_api.Tracer:
    provider = TracerProvider()
    provider.add_span_processor(create_tracing_pipeline())
    trace_api.set_tracer_provider(provider)
    tracer = trace_api.get_tracer(name, version)
    return tracer
