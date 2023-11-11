import babel


MONTHS = {
            1:'Jan',
            2: 'Feb',
            3: 'Mar',
            4: 'Apr',
            5: 'May',
            6: 'Jun',
            7: 'Jul',
            8: 'Aug',
            9: 'Sep',
            10: 'Oct',
            11: 'Nov',
            12: 'Dec',
          }

MONTHS_NUM = {
            'Jan': 1,
            'Feb': 2,
            'Mar': 3,
            'Apr': 4,
            'May': 5,
            'Jun': 6,
            'Jul': 7,
            'Aug': 8,
            'Sep': 9,
            'Oct': 10,
            'Nov': 11,
            'Dec': 12,
          }

def get_month_num(name) -> int:
  return MONTHS_NUM[name]

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