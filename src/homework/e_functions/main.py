#H4 main program

import value_return

epoch_seconds = 3800

hours = value_return.get_hour(epoch_seconds)
minutes = value_return.get_minutes(epoch_seconds)
seconds = value_return.get_seconds(epoch_seconds)

show_time = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
print("The time is:", show_time)