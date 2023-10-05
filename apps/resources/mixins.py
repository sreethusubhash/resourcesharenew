from rest_framework.exceptions import PermissionDenied
DEFAULT_CATEGORY_ID=1



class DenyDeletionOfDefaultCategoryMixin:
    # We want to get the category's id we r about to delete
    # We want to compare it with the DEFAULT_CATEGORY_ID
    # If True,we want raise an exception.
    #method to override get_queryset()
    #Method to used for listing
    def get_queryset(self):
        queryset =super().get_queryset()
        #breakpoint()
        if hasattr(self,'action') or self.action=='destroy':
            pk=self.kwargs['pk']
            deleted_queryset=queryset.get(pk=pk)
            if deleted_queryset.pk==DEFAULT_CATEGORY_ID:
                #raise an exception
                raise PermissionDenied(f'Not allowed to delete category with id {pk}')
            #Never forgot
            return queryset
def destroy(self,request,*args,**kwargs):
    pass
        