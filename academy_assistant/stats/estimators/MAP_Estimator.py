from scipy.optimize import minimize_scalar
from scipy.stats import norm



class MAP_Estimator:
    def __init__(self, item_response_vector, theta_dist=norm(0.5, 0.2)):
        """
            item_response_vector -> a list of touples: (item answer, IIIPL item model)
        """
        self.item_response_vector = item_response_vector
        self.theta_dist = theta_dist

    def likelihood_arr(self, thetas):
        values = []
        for theta in thetas:
            values.append(self.likelihood(theta) * -1.0)
        return values

    def likelihood(self, theta):
        # Two quiz questions
        # User 1 gets both correct

        # Say user ability level is 0.1
        # prob getting first correct is 0.5
        # prob getting second correct is 0.5
        # prob user gets both correct is 0.5 * 0.5 = 0.25

        # Say user ability level is 0.9 <-- this is theta
        # prob getting first correct is 0.9  <-- this is p(theta)
        # prob getting second correct is 0.9
        # prob user gets both correct is 0.9 * 0.9 = 0.81



        result = 1.0

        for item_tuple in self.item_response_vector:
            answer = int(item_tuple[0])
            item = item_tuple[1]
            if answer == 1:
                result = result * item.prob_correct(theta)
            else:
                result = result * (1.0 - item.prob_correct(theta))

        # Multiply likelihood by theta distribution
        result = result * self.theta_dist.pdf(theta)

        return result * -0.1

    def estimate(self):
        return minimize_scalar(self.likelihood, bounds=(0, 1), method='bounded')

