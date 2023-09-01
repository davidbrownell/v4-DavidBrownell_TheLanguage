# ----------------------------------------------------------------------
# |
# |  Build.py
# |
# |  David Brownell <db@DavidBrownell.com>
# |      2023-07-25 10:50:26
# |
# ----------------------------------------------------------------------
# |
# |  Copyright David Brownell 2023
# |  Distributed under the Boost Software License, Version 1.0. See
# |  accompanying file LICENSE_1_0.txt or copy at
# |  http://www.boost.org/LICENSE_1_0.txt.
# |
# ----------------------------------------------------------------------
# pylint: disable=missing-module-docstring

from pathlib import Path
from typing import Callable, Optional, TextIO, Tuple, Union

from Common_Foundation import PathEx
from Common_Foundation.Streams.DoneManager import DoneManager, DoneManagerFlags
from Common_Foundation import SubprocessEx

from Common_FoundationEx.BuildImpl import BuildInfoBase


# ----------------------------------------------------------------------
class BuildInfo(BuildInfoBase):
    # pylint: disable=missing-class-docstring

    # ----------------------------------------------------------------------
    def __init__(self):
        super(BuildInfo, self).__init__(
            name="TheLanguageGrammar",
            configurations=None,
            configuration_is_required_on_clean=None,
            requires_output_dir=False,
            suggested_output_dir_location=None,         # Optional[Path]
        )

    # ----------------------------------------------------------------------
    def Clean(                              # pylint: disable=arguments-differ
        self,
        configuration: Optional[str],       # pylint: disable=unused-argument
        output_dir: Optional[Path],         # pylint: disable=unused-argument
        output_stream: TextIO,              # pylint: disable=unused-argument
        on_progress_update: Callable[       # pylint: disable=unused-argument
            [
                int,                        # Step Index
                str,                        # Status Info
            ],
            bool,                           # True to continue, False to terminate
        ],
        *,
        is_verbose: bool,
        is_debug: bool,
    ) -> Union[
        int,                                # Return code
        Tuple[
            int,                            # Return code
            str,                            # Short status desc
        ],
    ]:
        with DoneManager.Create(
            output_stream,
            "",
            output_flags=DoneManagerFlags.Create(verbose=is_verbose, debug=is_debug),
        ) as dm:
            assert output_dir is None, output_dir
            output_dir = self._output_dir

            if not output_dir.exists():
                dm.WriteInfo("The directory '{}' does not exist.\n".format(output_dir))
            else:
                with dm.Nested("Removing '{}'...".format(output_dir)):
                    PathEx.RemoveItem(output_dir)

        return 0

    # ----------------------------------------------------------------------
    def Build(                              # pylint: disable=arguments-differ
        self,
        configuration: Optional[str],       # pylint: disable=unused-argument
        output_dir: Optional[Path],         # pylint: disable=unused-argument
        output_stream: TextIO,              # pylint: disable=unused-argument
        on_progress_update: Callable[       # pylint: disable=unused-argument
            [
                int,                        # Step Index
                str,                        # Status Info
            ],
            bool,                           # True to continue, False to terminate
        ],
        *,
        is_verbose: bool,
        is_debug: bool,
    ) -> Union[
        int,                                # Return code
        Tuple[
            int,                            # Return code
            str,                            # Short status desc
        ],
    ]:
        with DoneManager.Create(
            output_stream,
            "",
            output_flags=DoneManagerFlags.Create(verbose=is_verbose, debug=is_debug),
        ) as dm:
            assert output_dir is None, output_dir
            output_dir = self._output_dir

            command_line = 'java -jar antlr-4.13.0-complete.jar -Dlanguage=Python3 -o "{output_dir}" -no-listener -visitor "{input_file}"'.format(
                output_dir=output_dir,
                input_file=PathEx.EnsureFile(Path(__file__).parent.parent / "TheLanguageGrammar.g4"),
            )

            dm.WriteVerbose("Command Line: {}\n\n".format(command_line))

            result = SubprocessEx.Run(command_line)

            dm.result = result.returncode

            if dm.result != 0:
                dm.WriteError(result.output)

                if not dm.is_verbose:
                    dm.WriteInfo("\n\nCommand Line: {}\n\n".format(command_line))

            else:
                with dm.YieldVerboseStream() as stream:
                    stream.write(result.output)

                with (output_dir / "PylintVerifier-ignore").open("w") as f:
                    f.write("Ignore the generated content.\n")

            return dm.result

    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    # ----------------------------------------------------------------------
    @property
    def _output_dir(self) -> Path:
        return Path(__file__).parent.parent / "GeneratedCode"


# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
# ----------------------------------------------------------------------
if __name__ == "__main__":
    BuildInfo().Run()
