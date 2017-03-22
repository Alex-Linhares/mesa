import networkx as nx

from decimal import Decimal
from random import choice

from mesa import Agent, Model
from mesa.time import RandomActivation
from mesa.space import MesaNetwork


class VirusAgent(Agent):
    """ A virus agent, which can be infected or not infected. """

    def __init__(self, unique_id, infected=0):
        self.unique_id = unique_id
        self.infected = infected

    def step(self):
        # if self.infected is exposed, then check if
            # becomes infected
            # get neighbors, and make them exposed

        n_infected = 0
        print("here")
        print(self)
        #print(type(self.model.graph))
        #for neighbor in self.model.grid.neighbor_iter(self.pos):
            # TODO: switch self.infected to self.type for consistency
            # with other models -- ie Schelling.
        #     if neighbor.type == self.infected:
        #         n_infected += 1

        # # If unhappy, move:
        # if similar < self.model.homophily:
        #     self.model.grid.move_to_empty(self)
        # else:
        #     self.model.happy += 1

        pass

    def __str__(self):
        return "%s, %s" % (str(self.unique_id), self.infected)


class VirusModel(Model):
    """A virus model with some number of agents"""

    def __init__(self, N=150, width=500, height=500, avg_node_degree=3,
                 initial_outbreak_size=10):

        self.N = N
        self.avg_node_degree = Decimal(avg_node_degree)
        self.schedule = RandomActivation(self)
        self.initial_outbreak_size = initial_outbreak_size

        network = MesaNetwork(N, avg_node_degree=avg_node_degree)   # create G
        network = MesaNetwork.add_agents(network, VirusAgent)  # add agent objs
        network = self._infect_nodes(network, initial_outbreak_size)  # infect
        self.graph = network

        self.running = True

    def _infect_nodes(self, network, N):
        """ Infect nodes according to the initial outbreak size. """

        G = network
        for i in range(N):
            node = choice(G.nodes())
            G.node[node]['agent']['infected'] = 1
        return G

    def step(self):
        """Advance the model by one step."""
        '''
        Run one step of the model.
        '''
        # self.happy = 0  # Reset counter of happy agents
        self.schedule.step()
        # self.datacollector.collect(self)

        # If all agents are infected, halt the model.
        # if self.happy == self.schedule.get_agent_count():
        #     self.running = False
