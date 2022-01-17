from pywr.parameters import IndexParameter, Parameter, load_parameter
from pywr.recorders import Recorder, load_recorder, NodeRecorder, AggregatedRecorder, BaseConstantNodeRecorder
from pywr.recorders.events import EventRecorder, EventDurationRecorder
import numpy as np
import pandas

class DivisionAggregatedRecorder(Recorder):
    def __init__(self, model, recorder1, recorder2, **kwargs):
        super().__init__(model, **kwargs)
        self.recorder1 = recorder1
        self.recorder2 = recorder2
        self.children.add(recorder1)
        self.children.add(recorder2)
        self._values = None

    def reset(self):
        self._values =  np.zeros(len(self.model.scenarios.combinations)) 

    def finish(self):
        n = len(self.model.scenarios.combinations)
        value = self._values
        r1 = np.array(self.recorder1.values())
        r2 = np.array(self.recorder2.values())
        for i in range(n):
            if r2[i] == 0:
                value[i] = 1 #this is not true. Only for the resilience calculation
            else:
                value[i] = np.divide(r1[i],r2[i])
    
    def values(self):
        return self._values

    @classmethod
    def load(cls, model, data):
        recorder1 = data["recorder1"]
        recorder2 = data["recorder2"]
        return cls(model, recorder1, recorder2, **data)
DivisionAggregatedRecorder.register()   

class FakeYearIndexParameter(IndexParameter):
    """ 
        Clasifica una fecha cualquiera, situandola en alguno de los 6 periodos de planes de desarrollo
        Entrega un entero entre 0 y 7 donde 0 es antes de la semana 14 del 2020 y de 1 a 7 es segun PD
    """
    def __init__(self, model, dates, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.dates = dates        
    
    def index(self, timestep, scenario_index):
        
        for i, date in enumerate(self.dates):
            if timestep.datetime < date:
                return i
        else:
            raise ValueError('Simulation date "{}" is at or beyond final date "{}"'.format(timestep.datetime, self.dates[-1]))
        
    @classmethod
    def load(cls, model, data):
        
        dates = [pandas.to_datetime(d) for d in data.pop("dates")]
        return cls(model, dates, **data)
FakeYearIndexParameter.register()  

class FakeYearActivationParameter(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Base year to start the activation.
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)     
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year >= self.base_year.get_value(scenario_index):
                return 1
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
FakeYearActivationParameter.register() 

class LegumeCosts(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)     
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year == self.base_year.get_value(scenario_index):
                return 663866
            if timestep.year == self.base_year.get_value(scenario_index)+1:
                return 355589
            if timestep.year == self.base_year.get_value(scenario_index)+2:
                return 531783
            if timestep.year == self.base_year.get_value(scenario_index)+3:
                return 622603
            if timestep.year == self.base_year.get_value(scenario_index)+4:
                return 668614
            if timestep.year >= self.base_year.get_value(scenario_index)+5:
                return 709533
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
LegumeCosts.register() 

class LegumeIncome(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)     
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year == self.base_year.get_value(scenario_index):
                return 212532.5
            if timestep.year == self.base_year.get_value(scenario_index)+1:
                return 226425.3
            if timestep.year == self.base_year.get_value(scenario_index)+2:
                return 494432.9
            if timestep.year == self.base_year.get_value(scenario_index)+3:
                return 725287.7
            if timestep.year == self.base_year.get_value(scenario_index)+4:
                return 897498.3
            if timestep.year >= self.base_year.get_value(scenario_index)+5:
                return 985214.5
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
LegumeIncome.register()

class LegumeBenefits(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)     
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year == self.base_year.get_value(scenario_index):
                return -570324
            if timestep.year == self.base_year.get_value(scenario_index)+1:
                return -248154
            if timestep.year == self.base_year.get_value(scenario_index)+2:
                return -156341
            if timestep.year == self.base_year.get_value(scenario_index)+3:
                return -16306
            if timestep.year == self.base_year.get_value(scenario_index)+4:
                return 109892
            if timestep.year >= self.base_year.get_value(scenario_index)+5:
                return 156690
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
LegumeBenefits.register()

class CerealCosts(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)   
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year == self.base_year.get_value(scenario_index):
                return 616385
            if timestep.year == self.base_year.get_value(scenario_index)+1:
                return 308108
            if timestep.year == self.base_year.get_value(scenario_index)+2:
                return 484302
            if timestep.year == self.base_year.get_value(scenario_index)+3:
                return 575122
            if timestep.year == self.base_year.get_value(scenario_index)+4:
                return 621133
            if timestep.year >= self.base_year.get_value(scenario_index)+5:
                return 662052
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
CerealCosts.register()

class CerealIncome(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)   
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year == self.base_year.get_value(scenario_index):
                return 156608
            if timestep.year == self.base_year.get_value(scenario_index)+1:
                return 170500
            if timestep.year == self.base_year.get_value(scenario_index)+2:
                return 438508
            if timestep.year == self.base_year.get_value(scenario_index)+3:
                return 669363
            if timestep.year == self.base_year.get_value(scenario_index)+4:
                return 841573
            if timestep.year >= self.base_year.get_value(scenario_index)+5:
                return 929290
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
CerealIncome.register()

class CerealBenefits(IndexParameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """
    def __init__(self, model, base_year, *args, **kwargs):
        super().__init__(model, *args, **kwargs)
        self.base_year = base_year
        self.children.add(base_year)   
    
    def index(self, timestep, scenario_index):
            if timestep.year < self.base_year.get_value(scenario_index):
                return 0
            if timestep.year == self.base_year.get_value(scenario_index):
                return -561880
            if timestep.year == self.base_year.get_value(scenario_index)+1:
                return -239710
            if timestep.year == self.base_year.get_value(scenario_index)+2:
                return -147897
            if timestep.year == self.base_year.get_value(scenario_index)+3:
                return -7862
            if timestep.year == self.base_year.get_value(scenario_index)+4:
                return 118336
            if timestep.year >= self.base_year.get_value(scenario_index)+5:
                return 165133
    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        return cls(model, base_year, **data)
CerealBenefits.register()

class IntegerValue(Parameter):
    """Parameter that selects a float input and turns it into the integer value.
    ----------
    number : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """

    def __init__(self, model, number, **kwargs):
        super().__init__(model, **kwargs)
        self.number = number
        self.children.add(number)

    # def value(self, ts, si):
    #     return max(0, ts.year - self.base_year)
    
    # def calc_values(self, ts):
    #     n = self.__values.shape[0]
    #     for i in range(n):
    #         self.__values[i] = max(ts.year-self.base_year, self.piso)
    # def finish(self, ts):
    #     costs = np.zeros(len(self.model.scenarios.combinations))
    #     base_year = self.base_year.get_all_values()
        
    #     for i in range(len(costs)):
    #         if ts.year-base_year[i] >= 0:
    #             costs[i] = 1
    #         else:
    #             costs[i] = 0

    #     self._costs = costs

    # def values(self):
    #     return self._costs

    def value(self, ts, si):                                     
            return np.floor(self.number.get_value(si))  

    @classmethod
    def load(cls, model, data):
        number = load_parameter(model, data.pop("number"))
        return cls(model, number, **data)

IntegerValue.register()

class YearlyActivationParameter(Parameter):
    """Parameter that selects and year and produces a value of 1 for the rest of the timesteps from that year,
    in order to activate a measure in a randomly set year
    ----------
    base_year : parameter
        Discounting base year (i.e. the year with a discount factor equal to 1.0).
    """

    def __init__(self, model, base_year, piso, **kwargs):
        super().__init__(model, **kwargs)
        self.base_year = base_year
        self.piso = piso
        self.children.add(base_year)
        self.children.add(piso)

    # def value(self, ts, si):
    #     return max(0, ts.year - self.base_year)
    
    def calc_values(self, ts):
        n = self.__values.shape[0]
        for i in range(n):
            self.__values[i] = max(ts.year-self.base_year, self.piso)
    # def finish(self, ts):
    #     costs = np.zeros(len(self.model.scenarios.combinations))
    #     base_year = self.base_year.get_all_values()
        
    #     for i in range(len(costs)):
    #         if ts.year-base_year[i] >= 0:
    #             costs[i] = 1
    #         else:
    #             costs[i] = 0

    #     self._costs = costs

    # def values(self):
    #     return self._costs

    # def value(self, ts, si):                                     
    #         return max(self.piso, ts.year-self.base_year)  

    @classmethod
    def load(cls, model, data):
        base_year = load_parameter(model, data.pop("base_year"))
        piso = load_parameter(model, data.pop("piso"))
        return cls(model, base_year, piso, **data)

YearlyActivationParameter.register()

class StickyTrigger(Parameter):
    """
    Evalua si esta activo el contrato en esos 6 meses especificos. En caso de estarlo, entrega el valor del contrato
    """

    def __init__(self, model, storage_node, thresholds, contracts, **kwargs):
            super().__init__(model, **kwargs)
            for param in thresholds.values():
                param.parents.add(self)
            self.thresholds = thresholds
            
            for param in contracts.values():
                param.parents.add(self)
            self.contracts = contracts
            self.storage_node = storage_node

          # Internal state
            self._outcome = 0  # default not triggered
            self._last_week_evaluated = None
            self._last_year_evaluated = None                  

    def value(self, ts, si):
            week_no = ts.index % 52
            week_no += 1
            year_no = ts.index // 52
            year = self.model.timestepper.start.year + year_no                                      

            try:
                            threshold_parameter = self.thresholds[week_no]                                         
            except KeyError:
                return self._outcome
            else:
                # There is a threshold for this week
                if self._last_week_evaluated == week_no and self._last_year_evaluated == year:
                    # We've already evaluated this week
                                return self._outcome
                else:
                                # We need to evaluate the trigger for this threshold
                                current_volume = self.storage_node.volume[si.global_id]
                                threshold = threshold_parameter.get_value(si)
                                if current_volume < threshold:
                                                contract_parameter = self.contracts[week_no]
                                                contract_size = contract_parameter.get_value(si)
                                                self._outcome = contract_size
                                else:
                                                self._outcome = 0
                                self._last_week_evaluated = week_no
                                self._last_year_evaluated = year
                                return self._outcome                            

    @classmethod
    def load(cls, model, data):
        thresholds = {int(k): load_parameter(model, v) for k, v in data.pop('thresholds').items()}
        contracts = {int(k): load_parameter(model, v) for k, v in data.pop('contracts').items()}                          
        storage_node = model._get_node_from_ref(model, data.pop('storage_node'))
        return cls(model, storage_node, thresholds, contracts)
StickyTrigger.register()    

class AccumulatedIndexedArrayParameter(Parameter):
    """
    Guarda la cantidad de derechos comprados en los planes de desarrollo anteriores
    """
    def __init__(self, model, index_parameter, params, **kwargs):
        super().__init__(model, **kwargs)
        assert(isinstance(index_parameter, IndexParameter))
        self.index_parameter = index_parameter
        self.children.add(index_parameter)

        self.params = []
        for p in params:
            if not isinstance(p, Parameter):
                from pywr.parameters import ConstantParameter
                p = ConstantParameter(model, p)
            self.params.append(p)

        for param in self.params:
            self.children.add(param)
        self.children.add(index_parameter)

    def value(self, timestep, scenario_index):
        """Returns the value of the Parameter at the current index"""
        index = self.index_parameter.get_index(scenario_index)
        value = 0
        for i in range(index):
            value += self.params[i].get_value(scenario_index)
        return value

    @classmethod
    def load(cls, model, data):
        index_parameter = load_parameter(model, data.pop("index_parameter"))
        try:
            parameters = data.pop("params")
        except KeyError:
            parameters = data.pop("parameters")
        parameters = [load_parameter(model, parameter_data) for parameter_data in parameters]
        return cls(model, index_parameter, parameters, **data)
AccumulatedIndexedArrayParameter.register()

class ReservoirCostRecorder (Recorder):
    """
        Guarda el costo de construir el embalse, dependiendo de cuando se construye, considerando un periodo de DP antes
    """
    
    def __init__(self, model, construction_dp, capacity, discount_rate, **kwargs):
        super().__init__(model, **kwargs)
        self.construction_dp = construction_dp
        self.capacity = capacity
        self.children.add(construction_dp)
        self.children.add(capacity)
        self.discount_rate = discount_rate
        self._costs = None

    def finish(self):

        costs = np.zeros(len(self.model.scenarios.combinations))

        capacity = self.capacity.get_all_values()
        construction_dp = np.floor(self.construction_dp.get_all_values())
        
        for i in range(len(costs)):
            if construction_dp[i] > 6:
                costs[i] = 0
            else:
                decision_dp = int(construction_dp[i]) - 1
                discount_factor = 1 / (1 + self.discount_rate)**((decision_dp-1)*5)
                costs[i] = (335748.31*capacity[i]**0.342)*discount_factor

        self._costs = costs

    def values(self):
        return self._costs


    @classmethod
    def load(cls, model, data):

        construction_dp = load_parameter(model, data.pop("construction_dp"))
        capacity = load_parameter(model, data.pop("capacity"))
        return cls(model, construction_dp, capacity, **data)
ReservoirCostRecorder.register()

class PurchasesCostRecorder (Recorder):
    """
        Guarda el costo total de todas las compras de derechos
    """
    
    def __init__(self, model, purchases_value, discount_rate, **kwargs):
        super().__init__(model, **kwargs)
        self.purchases_value = purchases_value
        self.children.add(purchases_value)     
        self.discount_rate = discount_rate
        self._costs = None

    def finish(self):
        costs = np.zeros(len(self.model.scenarios.combinations))
        rendimiento10 = np.genfromtxt('R10.csv', delimiter=",", dtype="float", skip_header=1,usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))

        for dp_index, purchase in enumerate(self.purchases_value.params):
            if dp_index == 0:
                continue

            transacciones = purchase.get_all_values()
            timestep_index = (dp_index - 1) * 52 * 5
            discount_factor = 1 / (1 + self.discount_rate)**((dp_index-1)*5)

            for i in range(len(costs)):
                r10 = rendimiento10[timestep_index, i]
                if transacciones[i] > 0:
                    share_cost = np.exp(34.97656-0.6979327*np.log(0.12755444)+5.769883*np.log(r10))
                    transaction_cost = share_cost*0.12755444
                else: transaction_cost = 0
                costs[i] += transacciones[i] * transaction_cost * discount_factor

        self._costs = costs

    def values(self):
        return self._costs

    @classmethod
    def load(cls, model, data):

        purchases_value = load_parameter(model, data.pop("purchases"))
        return cls(model, purchases_value, **data)
PurchasesCostRecorder.register()

class SeasonRollingMeanFlowNodeRecorder(NodeRecorder):
    """Records the mean flow of a Node for the previous N timesteps for a specific season (april to october or october to april)

    Parameters
    ----------
    model : `pywr.core.Model`
    node : `pywr.core.Node`
        The node to record
    timesteps : int
        The number of timesteps to calculate the mean flow for
    name : str (optional)
        The name of the recorder

    """
    def __init__(self, model, node, first_week, last_week, years, **kwargs):
        super().__init__(model, node, **kwargs)
        self.first_week = first_week
        self.last_week = last_week
        self.years = years
        self.data = None

    def reset(self):
        super().reset()
        self.position = 0
        self.data = np.empty([len(self.model.timestepper), len(self.model.scenarios.combinations)])
        self._memory = np.zeros([len(self.model.scenarios.combinations), (self.last_week-self.first_week)*self.years])
        self.passed_weeks = 0

    def after(self):
        # calculates the week
        ts = self.model.timestepper.current
        week_no = ts.index % 52
        week_no += 1
        year_no = ts.index // 52
        year = self.model.timestepper.start.year + year_no   
        if self.first_week <= week_no < self.last_week:
            # save today's flow
            for i in range(0, self._memory.shape[0]):
                self._memory[i, self.position] = self.node.flow[i]
            self.passed_weeks += 1
            # calculate the mean flow
            n = self._memory.shape[1]
            if self.passed_weeks < n:
                n = self.passed_weeks
            # save the mean flow
            mean_flow = np.mean(self._memory[:, 0:n], axis=1)
            self.data[ts.index, :] = mean_flow
            # prepare for the next timestep
            self.position += 1
            if self.position >= self._memory.shape[1]:
                self.position = 0

    @classmethod
    def load(cls, model, data):
        node = model._get_node_from_ref(model, data.pop("node"))
        return cls(model, node, **data)
SeasonRollingMeanFlowNodeRecorder.register()

class ContractCostRecorder (Recorder):
    """
    Entrega el costo total relativo a los contratos segun fueron activados
    """
    def __init__(self, model, contract_value, purchases_value, discount_rate, week_no, temporada, total_shares = 8133, **kwargs):
        super().__init__(model, **kwargs)        
        self.contract_value = contract_value
        self.children.add(contract_value)
        self.purchases_value = purchases_value
        self.children.add(purchases_value)        
        self.discount_rate = discount_rate
        self.week_no = week_no
        self.temporada = temporada
        self.total_shares = total_shares
        self._costs = None

    def reset(self):
        self._costs = np.zeros(len(self.model.scenarios.combinations))   

    def after(self):
        # calculates the week
        ts = self.model.timestepper.current
        week_no = ts.index % 52
        week_no += 1
        year_no = ts.index // 52
        year = self.model.timestepper.start.year + year_no
        year_discount = max(0,year-2020)
        
        if week_no != self.week_no:
            return
        
        rabril = np.genfromtxt('RENDIMIENTOS_ABRIL.csv', delimiter=",", dtype="float", skip_header=1,usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
        roctubre = np.genfromtxt('RENDIMIENTOS_OCTUBRE.csv', delimiter=",", dtype="float", skip_header=1,usecols=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15))
        costs = self._costs
        shares = self.contract_value.get_all_values()
        purchases = self.purchases_value.get_all_values()
        discount_factor = 1 / (1 + self.discount_rate)**(year_discount)
        def pwise_invierno(x):
            if x>788.77:
                result=231443.69
            elif x>655.33:
                result=74.23*x+172982.97
            elif x>451.5:
                result=134.115*x+133648.95
            elif x>309.21:
                result=144.696*x+128871.63
            elif x>132.79:
                result=531.087*x+9396.48
            elif x>=0:
                result=601.85*x
            else: result = 0

            return result

        def pwise_verano(x):
            if x>1432.723:
                result=447932.13
            elif x>1194.12:
                result=601.85*x+341580.92
            elif x>921.077:
                result=134.115*x+270071.42
            elif x>621.145:
                result=144.696*x+260325.45
            elif x>287.162:
                result=531.087*x+20320.42
            elif x>=0:
                result=601.85*x
            else: result = 0

            return result

        def pwise_agro(x):
            if x>815.415:
                result=27201064
            elif x>536.824:
                result=305.565*x+26951901
            elif x>479.689:
                result=1911.5*x+26089797
            elif x>345.169:
                result=4237.767*x+24973912
            elif x>=320.469:
                result=7616.567*x+23807656    
            elif x>64.036:
                result=12192.388*x+22341248
            elif x>29.623:
                result=170359.239*x+12212897
            elif x>3.26:
                result=516658.723*x+1954546
            elif x>1.298:
                result=999687.896*x+380092
            elif x>=0:
                result=1292474.264*x
            else: result = 0

            return result


        if self.temporada == 1: #temporada de octubre
            for i in range(len(costs)):
                rendimiento_accion = roctubre[ts.index, i]
                compras_pasadas = purchases[i]
                acciones_regantes = max(8133-1917-compras_pasadas,0)
                acciones_contrato = min(acciones_regantes,shares[i]) 
                volumen_esperado = acciones_regantes*rendimiento_accion
                volumen_cambio = acciones_contrato*rendimiento_accion
                c = pwise_agro(volumen_esperado)-pwise_agro(volumen_esperado-volumen_cambio) + pwise_verano(volumen_esperado)-pwise_verano(volumen_esperado-volumen_cambio)
                costs[i] += c*discount_factor 

        elif self.temporada == 0: #temporada de abril
            for i in range(len(costs)):
                rendimiento_accion = rabril[ts.index, i]
                compras_pasadas = purchases[i]
                acciones_regantes = max(8133-1917-compras_pasadas,0)
                acciones_contrato = min(acciones_regantes,shares[i])
                volumen_esperado = acciones_regantes*rendimiento_accion
                volumen_cambio = acciones_contrato*rendimiento_accion
                c = pwise_invierno(volumen_esperado)-pwise_invierno(volumen_esperado-volumen_cambio)
                costs[i] += c*discount_factor
        else: print("error en la eleccion de temporada")

    def values(self):
        return self._costs

    @classmethod
    def load(cls, model, data):      
        contract_value = load_parameter(model, data.pop("contract"))
        purchases_value = load_parameter(model, data.pop("purchases"))
        return cls(model, contract_value, purchases_value, **data)
ContractCostRecorder.register()

class EventCountRecorder(Recorder):
    """ Recorder for the count of events found by an EventRecorder
    This Recorder uses the results of an EventRecorder to calculate the duration
    of those events in each scenario. Aggregation by scenario is done via
    the pandas.DataFrame.groupby() method.
    Any scenario which has no events will contain a NaN value.
    Parameters
    ----------
    event_recorder : EventRecorder
        EventRecorder instance to calculate the events.
    """

    def __init__(self, model, event_recorder, **kwargs):
        # Optional different method for aggregating across self.recorders scenarios
        agg_func = kwargs.pop('recorder_agg_func', kwargs.get('agg_func'))
        self.recorder_agg_func = agg_func

        super(EventCountRecorder, self).__init__(model, **kwargs)
        self.event_recorder = event_recorder
        self.event_recorder.parents.add(self)

    def setup(self):
        self._values = np.empty(len(self.model.scenarios.combinations))

    def reset(self):
        self._values[...] = 0.0

    def after(self):
        pass

    def values(self):
        return self._values

    def finish(self):
        df = self.event_recorder.to_dataframe()

        self._values[...] = 0.0
        # No events found
        if len(df) == 0:
            return

        for index, value in df['scenario_id'].value_counts().iteritems():
            self._values[index] = value
EventCountRecorder.register()

class DeficitFrequencySpecialNodeRecorder(BaseConstantNodeRecorder):
    """Recorder to return the frequency of timesteps with a failure to meet max_flow in a 1520 timesteps
    """

    def reset(self):
        self._values = np.zeros(len(self.model.scenarios.combinations))

    def after(self):
        node = self.node
        for scenario_index in self.model.scenarios.combinations:
            max_flow = node.get_max_flow(scenario_index)
            if abs(node.flow[scenario_index.global_id] - max_flow) > 1e-6:
                self._values[scenario_index.global_id] += 1.0
    
    def finish(self):
        self._values = self._values/1560

    def values(self):
        return self._values
DeficitFrequencySpecialNodeRecorder.register()

def CustomizedAggregation(model, weights):
    def weighted_agg_func(values):
        return np.dot(weights, values)
    model.recorders['Reliability'].agg_func = weighted_agg_func

    threshold = model.recorders["InstanstaneousDeficit"]
    failures = model.recorders["Weeks with deficit"]
    events = EventRecorder(model, threshold, name = "deficit_event")
    duration = EventDurationRecorder(model, events, name = "Max deficit duration [weeks]", recorder_agg_func = "max", agg_func = "mean", is_objective = "min")
    contara = EventCountRecorder(model,events, name = "Events of failures", agg_func = "mean")
    #resiliencia = AggregatedRecorder(model,[contara, failures], recorder_agg_func = np.divide, name = "Resilience", is_objective = 'max')
    resiliencia = DivisionAggregatedRecorder(model, contara, failures, name = "Resilience", agg_func = "mean", is_objective = 'max')

class MaximumDeficitNodeRecorder(NodeRecorder):
    """
    Recorder the maximum difference between modelled flow and max_flow for a Node
    """
    def reset(self):
        self._values = np.zeros(len(self.model.scenarios.combinations))   

    def after(self):
        ts = self.model.timestepper.current
        days = self.model.timestepper.current.days
        node = self.node
        values = self._values

        for scenario_index in self.model.scenarios.combinations:
            max_flow = node.get_max_flow(scenario_index)
            deficit = (max_flow - node.flow[scenario_index.global_id])*days
            if deficit > values[scenario_index.global_id]:
                values[scenario_index.global_id] = deficit

    def values(self):
        return self._values        
MaximumDeficitNodeRecorder.register()

class InstantaneousDeficictNodeRecorder(NodeRecorder):
    """
    Recorder the maximum difference between modelled flow and max_flow for a Node
    """
    def reset(self):
        self._values = np.zeros(len(self.model.scenarios.combinations))   

    def after(self):
        ts = self.model.timestepper.current
        days = self.model.timestepper.current.days
        node = self.node
        values = self._values

        for scenario_index in self.model.scenarios.combinations:
            max_flow = node.get_max_flow(scenario_index)
            deficit = (max_flow - node.flow[scenario_index.global_id])*days
            if deficit < 1e-4:
                deficit = 0
            values[scenario_index.global_id] = deficit

    def values(self):
        return self._values        
InstantaneousDeficictNodeRecorder.register()

class ReliabilityNodeRecorder(BaseConstantNodeRecorder):
    """Recorder to return the reliabity of a node
    """

    def reset(self):
        self._values = np.zeros(len(self.model.scenarios.combinations))

    def after(self):
        node = self.node
        for scenario_index in self.model.scenarios.combinations:
            max_flow = node.get_max_flow(scenario_index)
            if abs(node.flow[scenario_index.global_id] - max_flow) > 1e-6:
                self._values[scenario_index.global_id] += 1.0
    
    def finish(self):
        self._values = 1 - self._values/1560

    def values(self):
        return self._values
ReliabilityNodeRecorder.register()

class FailureCountRecorder(BaseConstantNodeRecorder):
    """Recorder to number of timesteps in failure
    """

    def reset(self):
        self._values = np.zeros(len(self.model.scenarios.combinations))

    def after(self):
        node = self.node
        for scenario_index in self.model.scenarios.combinations:
            max_flow = node.get_max_flow(scenario_index)
            if abs(node.flow[scenario_index.global_id] - max_flow) > 1e-6:
                self._values[scenario_index.global_id] += 1

    def values(self):
        return self._values
FailureCountRecorder.register()

