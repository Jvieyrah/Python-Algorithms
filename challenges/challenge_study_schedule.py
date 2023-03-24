def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    if not target_time:
        return None

    max_students = 0
    for period in permanence_period:
        if period[0] <= target_time < period[1]:
            students += 1

    return max_students