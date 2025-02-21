import flask_wtf

from wtforms import fields
from wtforms import validators


class AuthenticationForm(flask_wtf.FlaskForm):
    """Pide el padrón y la dirección de correo."""

    padron = fields.IntegerField(
        "Padrón",
        # validators=[validators.Regexp(r"\d+", message="Ingrese un padrón válido")],
    )

    email = fields.EmailField(
        "E-mail",
        validators=[validators.Email(message="Ingrese una dirección de e-mail válida")],
    )

    submit = fields.SubmitField("Obtener enlace")

    def _normalize_field(self, field: fields.Field) -> str:
        """Devuelve los datos del campo en minúsculas y sin espacio alrededor."""
        return field.data.strip().lower()

    def normalized_padron(self) -> str:
        return self.padron.data

    def normalized_email(self) -> str:
        return self._normalize_field(self.email)
