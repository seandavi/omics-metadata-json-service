resource "google_cloud_tasks_queue" "ncbi_eutils" {
  name = "ncbi-eutils"
  location = "us-central1"


  rate_limits {
    max_concurrent_dispatches = 20
    max_dispatches_per_second = 10
  }

  retry_config {
    max_attempts = 5
    max_retry_duration = "30s"
    max_backoff = "10s"
    min_backoff = "1s"
    max_doublings = 2
  }

  stackdriver_logging_config {
    sampling_ratio = 1.0
  }
}