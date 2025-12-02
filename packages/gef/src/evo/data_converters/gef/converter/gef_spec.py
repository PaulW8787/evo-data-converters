#  Copyright © 2025 Bentley Systems, Incorporated
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#      http://www.apache.org/licenses/LICENSE-2.0
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

# It should be noted here that the following column names are those provided
# by PyGef. If a column name maps to an empty string then this implies a
# dimensionless unit. Examples of dimensionless columns would be percentage
# values or ratios.
MEASUREMENT_UNITS: dict[str, str] = {
    "penetrationLength": "m",
    "coneResistance": "MPa",
    "localFriction": "MPa",
    "frictionRatio": "%",
    "porePressureU1": "MPa",
    "porePressureU2": "MPa",
    "porePressureU3": "MPa",
    "inclinationResultant": "degrees",
    "inclinationNS": "degrees",
    "inclinationEW": "degrees",
    "depth": "m",
    "elapsedTime": "s",
    "correctedConeResistance": "MPa",
    "netConeResistance": "MPa",
    "poreRatio": "",
    "coneResistanceRatio": "",
    "soilDensity": "kN/m3",
    "porePressure": "MPa",
    "verticalPorePressureTotal": "MPa",
    "verticalPorePressureEffective": "MPa",
    "inclinationX": "degrees",
    "inclinationY": "degrees",
    "electricalConductivity": "S/m",
    "magneticFieldStrengthX": "nT",
    "magneticFieldStrengthY": "nT",
    "magneticFieldStrengthZ": "nT",
    "magneticFieldStrengthTotal": "nT",
    "magneticInclination": "degrees",
    "magneticDeclination": "degrees",
}
