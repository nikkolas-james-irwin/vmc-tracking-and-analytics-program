# Returns the SQL query for total visits grouped by number of dependents based on user-provided location, from date, and to date
def get_query(from_time, to_time, substr):

    return "SELECT demographics.dependents, count(demographics.dependents) " \
           "FROM visits " \
           "LEFT JOIN demographics ON visits.student_id = demographics.student_id " \
           "where (location = \'" + substr + "\') and check_in_date >= \'" + from_time + "\' " \
            "and check_in_date <= \'" + to_time + "\' and demographics.dependents is not null group by demographics.dependents;"