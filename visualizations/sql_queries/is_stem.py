# Returns the SQL query for the total visits by stem major based on user-provided location, from date, and to date
def get_query(from_time, to_time, substr):
    return "SELECT demographics.is_stem, count(demographics.is_stem) " \
           "FROM visits LEFT JOIN demographics ON visits.student_id = demographics.student_id " \
           "WHERE (location = \'" + substr + "\') and check_in_date >= \'" + from_time + "\' " \
            "and demographics.is_stem is not null " \
            "AND check_in_date <= \'" + to_time + "\' and demographics.parent_education " \
                                                  "is not null GROUP BY demographics.is_stem;"