j = {
  'results': [
    {
      'address_components': [
        {
          'long_name': 'Babson College Drive',
          'short_name': 'Babson College Drive',
          'types': [
            'route'
          ]
        },
        {
          'long_name': 'Wellesley',
          'short_name': 'Wellesley',
          'types': [
            'locality',
            'political'
          ]
        },
        {
          'long_name': 'Norfolk County',
          'short_name': 'Norfolk County',
          'types': [
            'administrative_area_level_2',
            'political'
          ]
        },
        {
          'long_name': 'Massachusetts',
          'short_name': 'MA',
          'types': [
            'administrative_area_level_1',
            'political'
          ]
        },
        {
          'long_name': 'United States',
          'short_name': 'US',
          'types': [
            'country',
            'political'
          ]
        }
      ],
      'formatted_address': 'Babson College Drive, Wellesley, MA, USA',
      'geometry': {
        'bounds': {
          'northeast': {
            'lat': 42.299897,
            'lng': -71.26081599999999
          },
          'southwest': {
            'lat': 42.2964,
            'lng': -71.26977
          }
        },
        'location': {
          'lat': 42.298139,
          'lng': -71.26532929999999
        },
        'location_type': 'GEOMETRIC_CENTER',
        'viewport': {
          'northeast': {
            'lat': 42.299897,
            'lng': -71.26081599999999
          },
          'southwest': {
            'lat': 42.2964,
            'lng': -71.26977
          }
        }
      },
      'partial_match': True,
      'place_id': 'ChIJ07aZP0KB44kRSl1Z-EV_JyA',
      'types': [
        'route'
      ]
    }
  ],
  'status': 'OK'
}

# print(j['results'][0]['geometry']['location']['lat'])
print(j['results'][0])