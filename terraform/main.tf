

provider "google" {
  project = var.gcp_project
  region  = var.gcp_region
}


terraform {
 backend "gcs" {
   bucket  = "tf-store-omicidx-338300" 
   prefix  = "terraform/state"
 }
}

data "google_sql_database_instance" "main" {
  name = var.sql_instance_name
}


resource "google_sql_database" "db" {
  name     = var.sql_database_name 
  instance = data.google_sql_database_instance.main.name
}
