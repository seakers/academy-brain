from scipy.optimize import minimize_scalar
from scipy.optimize import minimize
import numpy as np
from scipy.stats import norm
from scipy.integrate import quad


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

    # Function to compute the probability of a correct answer using the 3PL model
    def prob_correct(self, theta, a, b, c):
        """
        Compute the probability of a correct answer using the 3PL model.

        :param theta: The ability level of the user.
        :param b: The difficulty parameter of the item.
        :return: The probability of a correct answer.
        """
        exp_component = np.exp(a * (theta - b))
        return c + (1 - c) * (exp_component / (1 + exp_component))

    # Function to compute the negative log posterior probability for parameters "a" and "b"
    def neg_log_posterior_ab(self, params, x, ab_dist, c_value):
        a, b = params  # Unpack the parameters
        def integrand(theta):
            return (self.prob_correct(theta, a, b, c_value) if x == 1 else (1 - self.prob_correct(theta, a, b, c_value))) * self.theta_dist.pdf(theta)
        
        # Integrating over a wide range instead of -inf to inf
        lower_bound, upper_bound = self.theta_dist.mean() - 200 * self.theta_dist.std(), self.theta_dist.mean() + 200 * self.theta_dist.std()
        integral, _ = quad(integrand, lower_bound, upper_bound)
        
        # Multiply likelihood with posterior probability density function for both "a" and "b"
        posterior_a = ab_dist[0].pdf(a)  # Prior for "a"
        posterior_b = ab_dist[1].pdf(b)  # Prior for "b"
        return -(np.log(posterior_a * posterior_b) + np.log(integral))  # Negative log for minimization

    # Function to calculate updated a and b parameter
    def update_ab_parameter(self, question_id, answer, a_value, b_value, c_value):
        c_value = c_value
        initial_params = [a_value, b_value]

        # Find normal distributions of initial "a" and "b", which are prior probabilities
        a_dist = norm(a_value, 2)  # Example standard deviation for "a"
        b_dist = norm(b_value, 0.2)
        ab_dist = [a_dist, b_dist]

        result = minimize(self.neg_log_posterior_ab, initial_params, args=(answer, ab_dist, c_value), method='L-BFGS-B', bounds=[(0, None), (0, 1)])
        
        # Update the estimated "a" and "b" parameters
        estimated_a, estimated_b = result.x
        return estimated_a, estimated_b