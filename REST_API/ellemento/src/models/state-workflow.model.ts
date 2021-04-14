import {Entity, model, property} from '@loopback/repository';

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
  next_state_type_id: number;

  @property({
    type: 'number',
    required: true,
  })
  source_location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  destination_location_id: number;

  @property({
    type: 'number',
    required: true,
  })
  duration_s: number;

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
