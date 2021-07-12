import pandas as pd
import numpy as np
from django.core.management import BaseCommand, CommandError

from asteroid.models import Sighting


class Command(BaseCommand):
    help = 'Enter the path of the file to import'

    def add_arguments(self, parser):
        parser.add_argument('path', nargs='+', type=str)

    def handle(self, *args, **options):
        path = options['path']
        try:

            df = pd.read_csv(path[0], delimiter='\t', header=0)

            for i, sighting in df.iterrows():
                num_rows, num_cols = sighting.loc["device_resolution"].split("x")

                list_values = np.array(list(sighting.loc['device_matrix'])).reshape(int(num_cols), int(num_rows))

                df_matrix = pd.DataFrame(list_values)
                df_matrix = df_matrix.replace("0", np.nan)
                df_matrix = df_matrix.dropna(how='all', axis=0)
                df_matrix = df_matrix.dropna(how='all', axis=1)
                df_matrix = df_matrix.replace(np.nan, "0")

                matrix_clear = "".join((np.array(df_matrix).reshape(1, df_matrix.size)[0]))

                Sighting.objects.create(
                    date=sighting.loc["date"],
                    time=sighting.loc["time"],
                    observatory_code=sighting.loc["observatory_code"],
                    device_code=sighting.loc["device_code"],
                    device_resolution=sighting.loc["device_resolution"],
                    device_matrix=sighting.loc["device_matrix"],
                    device_matrix_clear=matrix_clear
                )
        except Sighting:
            raise CommandError('Error')
