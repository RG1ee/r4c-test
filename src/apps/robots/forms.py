from django import forms

from src.apps.robots.models import Robot


class RobotForm(forms.ModelForm):
    class Meta:
        model = Robot
        fields = (
            "model",
            "version",
        )

    def clean(self):
        cleaned_data = super().clean()
        model = cleaned_data.get("model")
        version = cleaned_data.get("version")

        if Robot.objects.filter(model=model, version=version).exists():
            raise forms.ValidationError("Робот с такими данными уже существует.")

        return cleaned_data
