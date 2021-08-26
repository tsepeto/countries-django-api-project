import math


class DistanceCalculator():

    @staticmethod
    def calculate(modelA, modelB):
        """
            Finding the distance between two latitude-longitude coordinates involves 
            using the Haversine Formula. 
            This formula takes the curvature of the Earth into consideration,
            which is why it is significantly more accurate than the traditional distance formula.
            link:
            https://www.kite.com/python/answers/how-to-find-the-distance-between-two-lat-long-coordinates-in-python
        """

        # Radius of the Earth
        R = 6373.0


        # Coordinates
        latA = math.radians(modelA.latitude)
        lonA = math.radians(modelA.longitude)

        latB = math.radians(modelB.latitude)
        lonB = math.radians(modelB.longitude)

        # Change in coordinates
        dlat = latB - latA
        dlon = lonB - lonA

        # Haversine formula
        a = math.sin(dlat/2)**2 + math.cos(latA) * math.cos(latB) * math.sin(dlon / 2)**2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        distance = R * c

        return distance

