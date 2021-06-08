import {Entity, model, property, hasOne} from '@loopback/repository';
import {StateWorkflow} from './state-workflow.model';

@model({settings: {strict: false}})
export class Condition extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  condition_id?: number;

  @property({
    type: 'string',
    required: true,
  })
  condition_name: string;

  @property({
    type: 'string',
    required: true,
  })
  condition_property: string;

  @property({
    type: 'string',
  })
  condition_description?: string;

  @hasOne(() => StateWorkflow, {keyTo: 'condition_id'})
  stateWorkflow: StateWorkflow;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<Condition>) {
    super(data);
  }
}

export interface ConditionRelations {
  // describe navigational properties here
}

export type ConditionWithRelations = Condition & ConditionRelations;
