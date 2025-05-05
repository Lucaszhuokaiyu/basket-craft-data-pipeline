{{ config(materialized='view') }}

WITH source AS (
    SELECT * FROM raw.website_sessions
)

SELECT
    website_session_id,
    user_id,
    utm_campaign,
    utm_content,
    utm_source,
    device_type,
    http_referrer,
    is_repeat_session,
    created_at AS website_session_created_at,
    CURRENT_TIMESTAMP AS loaded_at
FROM source
