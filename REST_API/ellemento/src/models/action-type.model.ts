import {Entity, model, property, hasMany} from '@loopback/repository';
import {StateWorkflow} from './state-workflow.model';

@model({settings: {strict: false}})
export class ActionType extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  action_type_id?: number;

  @property({
    type: 'string',
    required: true,
  })
  action_name: string;

  @property({
    type: 'string',
    required: true,
  })
  description: string;

  @hasMany(() => StateWorkflow)
  stateWorkflows: StateWorkflow[];
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<ActionType>) {
    super(data);
  }
}

export interface ActionTypeRelations {
  // describe navigational properties here
}

export type ActionTypeWithRelations = ActionType & ActionTypeRelations;
