from ydata_profiling.report.presentation.core import FrequencyTable
from ydata_profiling.report.presentation.flavours.html import templates


class HTMLFrequencyTable(FrequencyTable):
    def render(self) -> str:
        if not isinstance(self.content["rows"][0], list):
            return templates.template("frequency_table.html").render(
                **self.content, idx=0
            )
        kwargs = self.content.copy()
        del kwargs["rows"]
        return "".join(
            templates.template("frequency_table.html").render(
                rows=rows, idx=idx, **kwargs
            )
            for idx, rows in enumerate(self.content["rows"])
        )
