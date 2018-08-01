# AllOfUs Client API
#
# The API used by AllOfUs workbench clients (including both notebooks and our UI.)
#
# OpenAPI spec version: 0.1.0
# 
# Generated by: https://github.com/swagger-api/swagger-codegen.git

#' @title Cohorts operations
#' @description swagger.Cohorts
#'
#' @field path Stores url path of the request.
#' @field apiClient Handles the client-server communication.
#' @field userAgent Set the user agent of the request.
#'
#' @importFrom R6 R6Class
#'
#' @section Methods:
#' \describe{
#'
#' materialize_cohort 
#'
#' }
#'
#' @export
CohortsApi <- R6::R6Class(
  'CohortsApi',
  public = list(
    userAgent = "Swagger-Codegen/1.0.0/r",
    apiClient = NULL,
    initialize = function(apiClient){
      if (!missing(apiClient)) {
        self$apiClient <- apiClient
      }
      else {
        self$apiClient <- ApiClient$new()
      }
    },
    materialize_cohort = function(workspace_namespace, workspace_id, request, ...){
      args <- list(...)
      queryParams <- list()
      headerParams <- character()

      if (!missing(`request`)) {
        body <- `request`$toJSONString()
      } else {
        body <- NULL
      }

      urlPath <- "/v1/workspaces/{workspaceNamespace}/{workspaceId}/materializeCohort"
      if (!missing(`workspace_namespace`)) {
        urlPath <- gsub(paste0("\\{", "workspaceNamespace", "\\}"), `workspace_namespace`, urlPath)
      }

      if (!missing(`workspace_id`)) {
        urlPath <- gsub(paste0("\\{", "workspaceId", "\\}"), `workspace_id`, urlPath)
      }

      resp <- self$apiClient$callApi(url = paste0(self$apiClient$basePath, urlPath),
                                 method = "POST",
                                 queryParams = queryParams,
                                 headerParams = headerParams,
                                 body = body,
                                 ...)
      
      if (httr::status_code(resp) >= 200 && httr::status_code(resp) <= 299) {
        returnObject <- MaterializeCohortResponse$new()
        result <- returnObject$fromJSON(httr::content(resp, "text", encoding = "UTF-8"))
        Response$new(returnObject, resp)
      } else if (httr::status_code(resp) >= 400 && httr::status_code(resp) <= 499) {
        Response$new("API client error", resp)
      } else if (httr::status_code(resp) >= 500 && httr::status_code(resp) <= 599) {
        Response$new("API server error", resp)
      }

    }
  )
)
