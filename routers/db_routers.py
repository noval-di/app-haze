from haze_traj.models import Haze_traj_db
from haze_traj.models import HotspotSipongi

class Auth:
    route_app_labels= {'admin, auth, contenttypes'}

    def db_for_read(self, model, **hints):

        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label in self.route_app_labels:
            return 'default'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label in self.route_app_labels or
            obj2._meta.app_label in self.route_app_labels
        ):
           return True
        return None

    # def allow_migrate(self, db, app_label, model_name=None, **hints):
    #     if app_label in self.route_app_labels:
    #         return False
    #     return False
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        
        if app_label in self.route_app_labels:
            return False
        return None

# class Haze_traj:
#     route_app_labels= {'haze_traj'}

#     def db_for_read(self, model, **hints):
#         if model._meta.app_label in self.route_app_labels:
#             return 'haze'
#         return None

#     # def db_for_write(self, model, **hints):
#     #     if model._meta.app_label in self.route_app_labels:
#     #         return 'default'
#     #     return None

#     def allow_relation(self, obj1, obj2, **hints):
#         if (
#             obj1._meta.app_label in self.route_app_labels or
#             obj2._meta.app_label in self.route_app_labels
#         ):
#            return True
#         return None

#     # def allow_migrate(self, db, app_label, model_name=None, **hints):
#     #     if app_label in self.route_app_labels:
#     #         return False
#     #     return False
    
#     def allow_migrate(self, db, app_label, model_name=None, **hints):
#         print(app_label)
#         print(self.route_app_labels)
#         print(db)
#         if app_label in self.route_app_labels:
#             print('testestestes')
#             return False
#         return False
class Haze_traj:
    route_app_labels= {'haze_traj'}

    def db_for_read(self, model, **hints):
        if model== Haze_traj_db:
            return 'haze'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return (db == 'default')
    
class Haze_traj_new:
    route_app_labels= {'haze_traj'}

    def db_for_read(self, model, **hints):
        if model== HotspotSipongi:
            return 'new_haze'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True
    
    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return (db == 'default')