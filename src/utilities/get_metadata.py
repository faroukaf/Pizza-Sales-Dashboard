import babel


MONTHS = {
            1:'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'June',
            7: 'July',
            8: 'Aug',
            9: 'Sept',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec',
          }

def get_months_names() -> dict[str]:
  return MONTHS

def get_sizes_name() -> dict[str]:
  return {
    'S': 'Small',
    'M': 'Medium',
    'L': 'Large',
    'XL': 'X-Large',
    'XXL': 'XX-Large'
  }