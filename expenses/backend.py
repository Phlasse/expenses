"""
Backend logic 
"""
import pandas as pd
import numpy as np
import os

class user_session:

    def __init__(
        self,
        user_id,
    ):
        self.sim_config = config
        self.setup_configs()

        self.pred_tickets = predicted_tickets
        self.prebooked = prebooked_tickets
        self.prebooked_rev = prebooked_rev

        # prebooked_tickets grouped by ticket_date
        self.grouped_prebooked = self._bin_days_new()
        self.bucket_vec = self._gen_bucket_vec()
        self.price_levels = self.sim_price_levels()

        self.price_per_level = self.update_price_card()

