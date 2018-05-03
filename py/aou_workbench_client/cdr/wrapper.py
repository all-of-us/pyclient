"""Wrapper class used by model objects to construct field names.
"""

class RelatedTableWrapper(object):
  def __init__(self, prefix, related_obj):
    self._prefix = prefix
    self._related_obj = related_obj

  def __getattr__(self, name):
    result = getattr(self._related_obj, name)
    if type(result) is RelatedTableWrapper:
      return RelatedTableWrapper(self._prefix + '.' + name, result._related_obj)
    return self._prefix + '.' + result