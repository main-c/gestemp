from enum import Enum


def build_tuple_types(enum_type):
    return tuple([(item.value, item.value) for item in enum_type])


# class RoleUtilisateur(str, Enum):
#     """Enumération des rôles utilisateurs."""

#     ADMINISTRATEUR = "administrateur"
#     RESPONSABLE = "responsable"
#     OBVERVATEUR = "observateur"


class GradeEnseignant(str, Enum):
    """Enumération des grades des enseignants."""

    ASSISTANT = "assistant"
    DOCTEUR = "docteur"
    PROFESSEUR = "professeur"


# ROLES_UTILISATEURS = build_tuple_types(RoleUtilisateur)
GRADES_ENSEIGNANTS = build_tuple_types(GradeEnseignant)
