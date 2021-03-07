from dataclasses import dataclass


@dataclass()
class ElementVariationSeries:
    min_interval: int
    max_interval: int
    relative_frequency: int
    accumulated_frequency: int
    particularity: float
    accumulated_particularity: float

    def values(self):
        return [f'{self.min_interval} - {self.max_interval}', f'{self.relative_frequency}',
                f'{self.particularity}',
                f'{self.accumulated_particularity}']
