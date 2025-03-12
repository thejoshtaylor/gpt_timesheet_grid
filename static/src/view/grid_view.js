/** @odoo-module **/

import { registry } from '@web/core/registry';
import { GridModel } from '../model/grid_model';
import { GridRenderer } from '../renderer/grid_renderer';
import { AbstractView } from '@web/views/abstract_view';

export class GridView extends AbstractView {
    static type = 'grid';
    static model = GridModel;
    static renderer = GridRenderer;
    static display_name = 'Grid';

    get archInfo() {
        return {
            adjust_field: this.props.arch.attrs.adjust_field || 'unit_amount',
            disable_linking: this.props.arch.attrs.disable_linking === 'true',
        };
    }
}

registry.category('views').add('grid', GridView);
