from fastapi.testclient import TestClient
from opentelemetry.trace import SpanKind
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from opentelemetry.sdk.trace.export.in_memory_span_exporter import InMemorySpanExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from src.app import app

def test_fastapi_instrumentation_with_in_memory_exporter():
    """
    Tests that the FastAPI instrumentation is working by manually setting up
    an in-memory exporter and checking that spans are created.
    """
    # Set up an in-memory exporter
    exporter = InMemorySpanExporter()
    processor = SimpleSpanProcessor(exporter)
    provider = TracerProvider()
    provider.add_span_processor(processor)

    # Instrument the app
    FastAPIInstrumentor.instrument_app(app, tracer_provider=provider)

    try:
        # Use the TestClient to make a request
        with TestClient(app) as client:
            client.get("/")

        # Check that a span was created
        spans = exporter.get_finished_spans()
        assert len(spans) > 0

        # The spans are not guaranteed to be in order, so we find the server span
        server_span = next((s for s in spans if s.kind == SpanKind.SERVER), None)

        assert server_span is not None, "Server span not found"
        assert server_span.name == "GET /"

        # http.method was deprecated in favor of http.request.method
        assert server_span.attributes.get("http.method") == "GET" or \
               server_span.attributes.get("http.request.method") == "GET"

        assert server_span.attributes.get("http.status_code") == 200 or \
               server_span.attributes.get("http.response.status_code") == 200

    finally:
        # Clean up instrumentation
        FastAPIInstrumentor.uninstrument_app(app)
