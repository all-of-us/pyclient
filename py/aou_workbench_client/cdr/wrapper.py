"""Wrapper class used by model objects to construct field names.
"""

class RelatedTableWrapper(object):
  def __init__(self, prefix, related_obj):
    self._prefix = prefix
    self._related_obj = related_obj

  def __getattr__(self, name):
    return self._prefix + getattr(self._related_obj, name)