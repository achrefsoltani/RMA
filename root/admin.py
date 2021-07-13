import actif.models
import impact.models
import menace.models
import mesure.models
import session.models
import vulnerabilite.models

from django.contrib import admin

# Register your models here.

admin.site.register(actif.models.typeActif)
admin.site.register(actif.models.actif)
admin.site.register(actif.models.actifCritique)

admin.site.register(impact.models.typeImpact)
admin.site.register(impact.models.impact)
admin.site.register(impact.models.impactNote)

admin.site.register(menace.models.menace)


admin.site.register(mesure.models.mesure)


admin.site.register(session.models.session)


admin.site.register(vulnerabilite.models.typeVulnerabilite)
admin.site.register(vulnerabilite.models.vulnerabilite)
admin.site.register(vulnerabilite.models.vulnerabiliteNote)



