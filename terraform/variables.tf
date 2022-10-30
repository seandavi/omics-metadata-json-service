variable "gcp_project" {
  type = string
  description = "The GCP project to deploy to"
}

variable "gcp_region" {
  type = string
  default = "us-central1"
  description = "The GCP region to deploy to"
}

variable "sql_instance_name" {
  type = string
  description = "The name of the PREEXISTING Cloud SQL instance to use (just the sql instance name, not the full connection string or fully qualified name)"
}

variable "sql_database_name" {
  type = string
  description = "The name of the database to create on the Cloud SQL instance"
}