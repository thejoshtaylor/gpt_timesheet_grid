/** @odoo-module **/

import { AbstractModel } from '@web/views/abstract_model';

export class GridModel extends AbstractModel {
    async load(params) {
        // Load data from the server based on params
        console.log("Loading grid data:", params);
        const result = await this.env.services.rpc('/grid/data', params);
        return result;
    }

    async reload(params) {
        return this.load(params);
    }
}
