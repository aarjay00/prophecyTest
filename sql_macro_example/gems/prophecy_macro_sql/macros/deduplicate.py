from dataclasses import dataclass

from prophecy.cb.sql.MacroBuilderBase import *
from prophecy.cb.ui.uispec import *


class Deduplicate1(MacroSpec):
    name: str = "deduplicate1"
    projectName: str = "macros_sql"
    category: str = "Custom"

    @dataclass(frozen=True)
    class Deduplicate1Properties(MacroProperties):
        macroName: str = ''
        projectName: str = ''
        parameters: list[MacroParameter] = field(default_factory=list)
	
    def dialog(self) -> Dialog:
        return Dialog("Macro") \
            .addElement(
            ColumnsLayout(gap="1rem", height="100%")
            .addColumn(
                Ports(allowInputAddOrDelete=True),
                "content"
            )
            .addColumn(
                StackLayout(height="100%")
		.addElement(NativeText("Custom Deduplicate1 Macro UI"))
		.addElement(
                MacroInstance(
                    "Macro Parameters",
                    name="component.properties.macroName",
                    projectName="component.properties.projectName"
                    ).bindProperty("parameters").withSchemaSuggestions()
                ),
                "2fr"
            )
        )                   
