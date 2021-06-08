import {Entity, model, property, hasMany} from '@loopback/repository';
import {State} from './state.model';

@model({settings: {strict: false}})
export class StateWorkflow extends Entity {
  @property({
    type: 'number',
    id: true,
    generated: true,
  })
  state_type_id?: number;

  @property({
    type: 'number',
    required: true,
  })
  stage_id: number;

  @property({
    type: 'number',
    required: true,
  })
  action_type_id: number;
  
  @property({
    type: 'number',
    required: true,
  })
  condition_id: number;

  @property({
    type: 'number',
    required: true,
  })
  next_state_type_id: number;
  
  @property({
    type: 'number',
    required: true,
  })
  next_state_type_id_2: number;

  @property({
    type: 'number',
    required: true,
  })
  source_id: number;

  @property({
    type: 'number',
    required: true,
  })
  destination_id: number;

  @property({
    type: 'number',
    required: true,
  })
  duration_s: number;
  
  @property({
    type: 'date',
    required: true,
  })
  validity_date_time_start: string;

  @property({
    type: 'date',
    required: true,
  })
  validity_date_time_end: string;

  @hasMany(() => State, {keyTo: 'state_type_id'})
  states: State[];

  @property({
    type: 'number',
  })
  stageId?: number;

  @property({
    type: 'number',
  })
  actionTypeId?: number;
  // Define well-known properties here

  // Indexer property to allow additional data
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  [prop: string]: any;

  constructor(data?: Partial<StateWorkflow>) {
    super(data);
  }
}

export interface StateWorkflowRelations {
  // describe navigational properties here
}

export type StateWorkflowWithRelations = StateWorkflow & StateWorkflowRelations;
