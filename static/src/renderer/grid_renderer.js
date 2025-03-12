/** @odoo-module **/

import { Component, useState } from '@odoo/owl';

export class GridRenderer extends Component {
    setup() {
        this.state = useState({
            data: this.props.data,
        });
    }

    render() {
        console.log("Rendering grid with data:", this.state.data);
        return (
            <table className="o_grid">
                <thead>
                    <tr>
                        <th>Date</th>
                        <th>Project</th>
                        <th>Task</th>
                        <th>Unit Amount</th>
                    </tr>
                </thead>
                <tbody>
                    {this.state.data.map((line) => (
                        <tr key={line.id}>
                            <td>{line.date}</td>
                            <td>{line.project_id?.name}</td>
                            <td>{line.task_id?.name}</td>
                            <td>{line.unit_amount}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        );
    }    
}

GridRenderer.template = 'gpt_timesheet_grid.GridRenderer';
