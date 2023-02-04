from django import forms

# validators method
def validate_for_a(value):
    if value[0]=='a' or value[0]=='A':
        raise forms.ValidationError('name should not start with a')
def forlen(value):
    if len(value)<5:
        raise forms.ValidationError('length is low')
    
    
    
class RegistrationForm(forms.Form):
    name  =     forms.CharField(max_length=100,validators=[validate_for_a,forlen]) 
    age   =     forms.IntegerField()
    email =    forms.EmailField(max_length=100)
    re_email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=10,widget=forms.PasswordInput)
    re_enter_password = forms.CharField(max_length=10,widget=forms.PasswordInput)
    bot = forms.CharField( max_length=50, required=False,widget=forms.HiddenInput)
    
    def clean(self):
        e = self.cleaned_data['email']
        r = self.cleaned_data['re_email'] 
        p = self.cleaned_data['password']
        re_Pass = self.cleaned_data['re_enter_password']
        
        if e!=r:
            raise forms.ValidationError('not matched')
        
        elif p!=re_Pass:
            raise forms.ValidationError('not matched')
        
        
        def clean_bot(self):
            bot = self.cleaned_data['bot']
            
            if len(bot)>0:
                raise forms.ValidationError('Bot catched')
        def  clean_age(self):
            a = self.cleaned_data['age']
            if a >= 18:
                raise forms.ValidationError('not eligible')
                    
               
            
        






    
    