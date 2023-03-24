def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    max_students = 0
    for period in permanence_period:
        try:
            if type(period[0]) != int or type(period[1]) != int:
                return None
            if period[0] <= target_time <= period[1]:
                max_students  += 1
        except TypeError:
            return None
    return max_students
