from app.services.note_service import generate_summary


def test_summary_generating():
    summary_text = generate_summary("Just a test note")
    assert summary_text[:13] != "Summary failed:"
