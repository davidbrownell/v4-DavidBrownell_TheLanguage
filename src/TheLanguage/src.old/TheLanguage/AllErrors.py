# ----------------------------------------------------------------------
# |
# |  AllErrors.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-08-08 15:31:04
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
"""Contains all errors generated by TheLanguage"""

from pathlib import Path

from TheLanguage.Common.Errors import CreateErrorType


# ----------------------------------------------------------------------
IncludeInvalidWorkspaceRoot                 = CreateErrorType("The filename or directory '{name}' is not contained within a workspace or include root.", name=Path)
IncludeInvalidSourceDirectory               = CreateErrorType("The directory '{name}' does not exist.", name=Path)
IncludeInvalidSourceGeneric                 = CreateErrorType("The filename or directory '{name}' does not exist.", name=Path)
IncludeInvalidFilename                      = CreateErrorType("The filename '{name}' does not exist.", name=Path)

InvalidClassIdentifier                      = CreateErrorType("'{name}' is not a valid class name.", name=str)
InvalidComponentIdentifier                  = CreateErrorType("'{name}' is not a valid component name.", name=str)
InvalidFileOrDirectoryIdentifier            = CreateErrorType("'{name}' is not a valid file or directory name,", name=str)
InvalidFunctionIdentifier                   = CreateErrorType("'{name}' is not a valid function name.", name=str)
InvalidTemplateIdentifier                   = CreateErrorType("'{name}' is not a valid template name.", name=str)
InvalidTypeIdentifier                       = CreateErrorType("'{name}' is not a valid type name.", name=str)
InvalidVariableIdentifier                   = CreateErrorType("'{name}' is not a valid variable name.", name=str)