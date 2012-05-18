from boto.dynamodb import connect_to_region

from server_config import db_config

def ConnectDB():
    return connect_to_region( 'eu-west-1',
                aws_access_key_id=db_config['AWS_ACCESS_KEY_ID'],
                aws_secret_access_key=db_config['AWS_SECRET_ACCESS_KEY']
            )

#class ValidationError(Exception):
#    """
#    Raised when a validator fails to validate its input.
#    """
#    pass

#class DynamoModel(object):
#    def __init__(self, **kw):
#        for key, value in kw.iteritems():
#            self[key] = value
        

#class ValidationError(Exception):
#    """
#    Raised when a validator fails to validate its input.
#    """
#    pass
#
#class Property(object):
#    def __init__(self, verbose_name=None, default=None, required=False):
#        self.default = default
#        self.required = required
#        self.verbose_namae = verbose_name
#    
#    def validate(self, value):
#        if not value:
#            if self.required:
#                raise ValidationError('Property %s is required' % self.name)
#            
#    def default_value(self):
#        return self.default
#            
#class StringProperty(Property):
#    
#    MAX_LENGTH = 500
#    
#    def __init__(self, verbose_name=None, **kwds):
#        super(StringProperty, self).__init__(verbose_name, **kwds)
#    
#    def validate(self, value):
#        value = super(StringProperty, self).validate(value)
#        if value is not None and not isinstance(value, basestring):
#            raise ValidationError(
#                                  'Property %s must be a str or unicode instance, not a %s'
#                                  % (self.name, type(value).__name__))
#        if value is not None and len(value) > self.MAX_LENGTH:
#            raise ValidationError(
#                                  'Property %s is %d characters long; it must be %d or less.'
#                                  % (self.name, len(value), self.MAX_LENGTH))
#        return value
#    
#class TextProperty(StringProperty):
#    
#    MAX_LENGTH = 65536
#    
#class DateTimeProperty(Property):
#    def __init__(self, verbose_name=None, auto_now=False, auto_now_add=False, **kwds):
#        super(DateTimeProperty, self).__init__(verbose_name, **kwds)
#        self.auto_now = auto_now
#        self.auto_now_add = auto_now_add
#
#    def validate(self, value):
#        value = super(DateTimeProperty, self).validate(value)
#        if value and not isinstance(value, datetime.datetime):
#            raise ValidationError('Property %s must be a %s' %
#                              (self.name, datetime.datetime.__name__))
#        return value
#    
#    def default_value(self):
#        if self.auto_now or self.auto_now_add:
#            return self.now()
#        return Property.default_value(self)
#    
#    def _now(self):
#        return datetime.datetime.now()
#
#class DynamoModel(object):
#    pass