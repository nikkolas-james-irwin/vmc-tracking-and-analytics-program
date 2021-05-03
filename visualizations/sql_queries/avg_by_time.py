# Returns the SQL query for the average visits by time based on user-provided location, from date, and to date
def get_query(from_time, to_time, substr):
    return "SELECT cat_hours.hour_display, round(IFNULL(SUM(c_visits.visit_count), 0)/(julianday('" + to_time + "') " \
        "- julianday('" + from_time + "')), 2) FROM cat_hours LEFT JOIN " \
        "(SELECT LTRIM(SUBSTR(check_in_time,1,2),'0') || ' ' || SUBSTR(check_in_time,7,2) " \
        "AS hour_display, 1 AS visit_count, check_in_date FROM visits WHERE (location = '" + substr + "') " \
        "and check_in_date BETWEEN '" + from_time + "' AND '" + to_time + "') AS c_visits ON " \
        "cat_hours.hour_display = c_visits.hour_display GROUP BY cat_hours.hour_display ORDER BY " \
                                                                          "cat_hours.ordering;"