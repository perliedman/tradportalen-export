#!/usr/bin/python3

import xml.etree.ElementTree as ET
import json

def item_to_property(item):
  types = [int, float, str]
  def try_types(v):
    for t in types:
      try:
        return t(v)
      except ValueError:
        pass
      except TypeError:
        pass
    return v

  if len(item) > 0:
    return dict([(i.tag, item_to_property(i)) for i in item])
  else:
    return try_types(item.text)

def convert(src, dst):
  tree = ET.parse(src)
  root = tree.getroot()

  features = []
  for observation in root.findall('./TreeObservation'):
    properties = item_to_property(observation)

    location = properties['Location']

    feature = {
      'type': 'Feature',
      'properties': properties,
      'geometry': {
        'type': 'Point',
        'coordinates': [location['Longitude'], location['Latitude']]
      }
    }

    features.append(feature)

  json.dump({
    'type': 'FeatureCollection',
    'features': features
  }, dst)

if __name__ == '__main__':
  import sys
  import os.path

  for path in sys.argv[1:]:
    with open(path, 'r') as src:
      head, tail = os.path.split(path)
      name, _ = os.path.splitext(tail)
      dst_path = os.path.join(head, name + '.json')
      with open(dst_path, 'w') as dst:
        print('Converting %s to %s' % (path, dst_path))
        convert(src, dst)
